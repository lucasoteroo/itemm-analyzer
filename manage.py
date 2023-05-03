# -*- coding: utf-8 -*-
import app

from flask.cli import FlaskGroup

cli = FlaskGroup(app)


@cli.command("create_user")
def create_admin():
    """Criar um usuario."""
    app.create_user()


if __name__ == "__main__":
    cli()
