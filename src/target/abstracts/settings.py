from abc import abstractmethod
from ..interfaces import ISettings


class AbstractSettings(ISettings):
    """
    Description:
    ------------
    設定の基底クラス
    """

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def action_limit(self):
        pass

    @property
    def step_limit(self):
        return self.action_limit * 5

    @property
    @abstractmethod
    def perception_number(self):
        pass

    @property
    @abstractmethod
    def action_number(self):
        pass

    @property
    def fps(self):
        return 8
