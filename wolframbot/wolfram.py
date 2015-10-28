import wolframalpha
from hamper.interfaces import Command, ChatCommandPlugin


class Wolfram(ChatCommandPlugin):
    """Query Wolfram Alpha for math, stats, etc."""
    name = 'wolfram'

    priority = 2

    def setup(self, loader):
        try:
            self.api_key = loader.config['wolfram']['api_key']
        except KeyError:
            print('To use the Wolfram Alpha plugin you must set the api key'
                  '\n in your config file:'
                  '\nExample:'
                  '\nwolfram:'
                  '\n    api_key: FOOBAR')

    def _run_query(self, query):
        client = wolframalpha.Client(self.api_key)
        res = client.query(query)
        try:
            return "{} | https://wolframalpha.com".format(next(res.results).text)
        except StopIteration as e:
            return 'No results found.'

    class WolframAlpha(Command):
        regex = 'wa (.+)'

        def command(self, bot, comm, groups):
            bot.reply(comm, self.plugin._run_query(groups[0]))
