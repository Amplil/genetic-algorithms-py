from target import AbstractGymTarget
from .settings import Settings
from .ga_settings import GaSettings


class CartPole(AbstractGymTarget):
    """
    Description:
    ------------
    Cart Pole
    """

    def __init__(self):
        super().__init__('CartPole-v1', Settings, GaSettings)

    def clone(self):
        return CartPole()

    def _perform_perceive(self, index):
        return self.observation[index] < 0

    def _perform_get_fitness(self):
        return self.action_step / self.settings.action_limit + (1 - abs(self.observation[0]) / 2.4) * 0.01
