import click
import boto3


def add(x, y):
    return x + y


@click.command()
def buckets():
    """This lists all my AWS buckets"""

    s3 = boto3.client("s3")
    s3buckets = s3.list_buckets()
    click.echo(click.style(f"List of buckets: {s3buckets}", bg="white", fg="black"))


if __name__ == "__main__":
    buckets()
