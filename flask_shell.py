import os
import sys

import click
from flask.cli import with_appcontext


@click.command('shell', short_help='Runs a shell in the app context.')
@click.option('--ptipython/--no-ptipython', default=True)
@click.option('--ptpython/--no-ptpython', default=True)
@click.option('--ipython/--no-ipython', default=True)
@click.option('--bpython/--no-bpython', default=True)
@with_appcontext
def shell_command(ptipython, ptpython, ipython, bpython):
    """Runs an interactive Python shell in the context of a given
    Flask application.  The application will populate the default
    namespace of this shell according to it's configuration.
    This is useful for executing small snippets of management code
    without having to manually configuring the application.
    """
    import code
    from flask.globals import _app_ctx_stack
    app = _app_ctx_stack.top.app
    banner = 'Python %s on %s\nApp: %s%s\nInstance: %s' % (
        sys.version,
        sys.platform,
        app.import_name,
        app.debug and ' [debug]' or '',
        app.instance_path,
    )
    ctx = {}
    startup = os.environ.get('PYTHONSTARTUP')
    if startup and os.path.isfile(startup):
        with open(startup, 'r') as f:
            eval(compile(f.read(), startup, 'exec'), ctx)

    ctx.update(app.make_shell_context())

    if ptipython:
        try:
            from ptpython.ipython import embed
            embed(banner1=banner, user_ns=ctx)
            return
        except ImportError:
            pass

    if ptpython:
        try:
            from ptpython.repl import embed
            embed(globals=ctx)
            return
        except ImportError:
            pass

    if ipython:
        try:
            from IPython import embed
            embed(banner1=banner, user_ns=ctx)
            return
        except ImportError:
            pass

    if bpython:
        try:
            from bpython import embed
            embed(banner=banner, locals_=ctx)
            return
        except ImportError:
            pass

    code.interact(banner=banner, local=ctx)
