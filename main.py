import argh
from tqdm import tqdm

@argh.named('tqdm')
def tqdm_demo():
    """tqdm - means "progress" in Arabic and is an abbreviation for "I love you so much" in Spanish."""

    for _ in tqdm(range(int(1e7)), desc='Progress#1'):
        pass


def greet(name = 'world'):
    """Greeting to the world."""

    return 'Hello, {0}!'.format(name)


@argh.arg('name', choices=['you', 'all'])
def reply(name):
    """Reply to you or to all."""

    return 'Hi, {0}!'.format(name)


if __name__ == '__main__':
    argh.dispatch_commands([
        tqdm_demo,
        greet,
        reply,
        ])
