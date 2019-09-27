class SystemStatus:
    def __init__(self, url, status='404'):
        self.url = url
        self.status = status

    def __str__(self):
        return "Url: %s ; Status: %s" % (
            self.url,
            self.status)
