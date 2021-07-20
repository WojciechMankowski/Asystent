class IncomprehensionException(Exception):
    def __init__(self):
        super(IncomprehensionException, self).__init__("Nie mogę się zrozumieć.")
class NoCommandException(Exception):
    def __init__(self, commend):
        super(NoCommandException, self).__init__(f"Brak tej komendy: {commend}")
