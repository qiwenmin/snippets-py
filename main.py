import argh

def greet(name = 'world'):
    """Greeting to the world."""

    return 'Hello, {0}!'.format(name)


@argh.arg('name', choices=['you', 'all'])
def reply(name):
    """Reply to you or to all."""

    return 'Hi, {0}!'.format(name)


if __name__ == '__main__':
    argh.dispatch_commands([
        greet,
        reply,
        ])
