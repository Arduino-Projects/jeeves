from core.strategy_impl.read_emails import ReadEmails
from .strategy_impl.play_music import PlayMusic
from .strategy_impl.start_tv import StartTV
from .strategy_impl.order_pizza import OrderPizza
from .strategy_impl.order_food import OrderFood
from .strategy_impl.open_facebook import OpenFacebook
from .strategy_impl.control_ac import ControlAC
from .strategy_impl.control_fan import ControlFan
from .strategy_impl.suggest_restaurant import SuggestRestaurant
from .strategy_impl.make_coffee import MakeCoffee
from .strategy_impl.suggest_recipe import SuggestRecipe
from .strategy_impl.read_news_and_weather import ReadNewsAndWeather

strategies = {
    "feel": {
        "bored": [PlayMusic(), StartTV()],
        "hungry": [OrderPizza(), OrderFood()],
        "lonely": [OpenFacebook()],
        "hot": [ControlAC()],
        "warm": [ControlAC(), ControlFan()],
        "cold": [ControlAC()]
    },
    "need": {
        "food": [SuggestRestaurant(), SuggestRecipe()],
        "coffee": [MakeCoffee()],
        "news": [ReadNewsAndWeather()],
        "emails": [ReadEmails()],
        "mails": [ReadEmails()]
    }
}
