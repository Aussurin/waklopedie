from flask import current_app
from flask.cli import AppGroup

from apps.main import create_app



app = create_app()

manage_cli = AppGroup("manage")


@manage_cli.command('list_routes')
def list_routes():
    """
    List routes exposed by the application
    """
    routes = []
    for route in current_app.url_map.iter_rules():
        routes.append(
            '{} ({}) ==> {}'.format(
                route.rule,
                ', '.join(sorted(route.methods)),
                route.endpoint
            )
        )
    for route in sorted(routes):
        print(route)

app.cli.add_command(manage_cli)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)