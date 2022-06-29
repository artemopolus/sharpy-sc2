import random

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:
    from sharpy.knowledges import SkeletonBot

val = random.randint(0, 5)
LadderBot: Type["SkeletonBot"]
if val == 0:
    from .lings import LadderBot
elif val == 1:
    from .macro_roach import LadderBot
elif val == 2:
    from .macro_zerg_v2 import LadderBot
elif val == 3:
    from .mutalisk import LadderBot
elif val == 4:
    from .roach_hydra import LadderBot
elif val == 5:
    from .twelve_pool import LadderBot


class RandomZergBot(LadderBot):  # type: ignore
    pass
