import pytest

from r2d7.listformatter import ListFormatter
from r2d7.slackprinter import SlackPrinter

class DummyBot(ListFormatter, SlackPrinter):
    pass

get_xws_tests = (
    (
        "http://geordanr.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!248::50:-1:&sn=Sunny%20B!&obs=",
        {"faction":"scum","pilots":[{"name":"sunnybounder","ship":"m3ainterceptor","upgrades":{"title":["lightscykinterceptor"]}}],"vendor":{"yasb":{"builder":"(Yet Another) X-Wing Miniatures Squad Builder","builder_url":"https://geordanr.github.io/xwing","link":"https://geordanr.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!248::50:-1:&sn=Sunny%20B!&obs="}},"version":"0.3.0","name":"Sunny B!"},
    ),
)

@pytest.mark.parametrize('url, expected', get_xws_tests)
def test_get_xws(url, expected):
    bot = DummyBot()
    assert bot.get_xws(url) == expected

print_tests = (
    (
        {"faction":"scum","pilots":[{"name":"sunnybounder","ship":"m3ainterceptor","upgrades":{"title":["lightscykinterceptor"]}}],"vendor":{"yasb":{"builder":"(Yet Another) X-Wing Miniatures Squad Builder","builder_url":"https://geordanr.github.io/xwing","link":"https://geordanr.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!248::50:-1:&sn=Sunny%20B!&obs="}},"version":"0.3.0","name":"Sunny B!"},
        [
            #TODO links
            ':scum: *Sunny B!* *[12]*',
            ':m3ainterceptor::skill1: _Sunny Bounder_: "Light Scyk" Interceptor *[12]*',
        ],
    ),
    (
        {"faction":"scum","pilots":[{"name":"cartelmarauder","ship":"kihraxzfighter","upgrades":{"missile":["homingmissiles"],"illicit":["hotshotblaster"],"mod":["engineupgrade","stealthdevice","shieldupgrade"],"title":["vaksai"]}}],"vendor":{"yasb":{"builder":"(Yet Another) X-Wing Miniatures Squad Builder","builder_url":"https://geordanr.github.io/xwing","link":"https://geordanr.github.io/xwing/?f=Scum%20and%20Villainy&d=v4!s!138:17,113:54:2:M.3,M.1&sn=Sunny%20B!&obs="}},"version":"0.3.0","name":"Vaksai!"},
        [
            ':scum: *Vaksai!* *[34]*',
            ':kihraxzfighter::skill2: _Cartel Marauder_: Homing Missiles, "Hot Shot" Blaster, Engine Upgrade, Stealth Device, Shield Upgrade, Vaksai *[34]*',
        ],
    ),
    (
        {"faction":"imperial","pilots":[{"name":"darthvader","ship":"tieadvanced","upgrades":{"system":["accuracycorrector"],"title":["tiex1"]}}],"vendor":{"yasb":{"builder":"(Yet Another) X-Wing Miniatures Squad Builder","builder_url":"https://geordanr.github.io/xwing","link":"https://geordanr.github.io/xwing/?f=Galactic%20Empire&d=v4!s!22:-1,-1:23:-1:U.107&sn=TIE%2FX1&obs="}},"version":"0.3.0","name":"TIE/X1"},
        [
            ':imperial: *TIE/X1* *[29]*',
            ':tieadvanced::skill9: _Darth Vader_: Accuracy Corrector, TIE/x1 *[29]*',
        ],
    ),
)

@pytest.mark.parametrize('xws, expected', print_tests)
def test_print(xws, expected):
    bot = DummyBot()
    assert bot.print(xws) == expected
