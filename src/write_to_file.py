import click


@click.command()
@click.option('--status', default='some status')
def main(status: str):
    with open('./INFO.txt', 'w+') as f:
        f.write(status)


if __name__ == "__main__":
    main()
