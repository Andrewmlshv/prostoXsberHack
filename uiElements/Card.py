from typing import List

from uiElements.Button import Button
from uiElements.Container import Container
from uiElements.UIClick import UIClick
from uiElements.EditTextField import EditTextField
from uiElements.Image import Image
from uiElements.TextField import TextField


class Card(Container, UIClick):
    def __init__(self, ord_par, texts_par: List[TextField], edits_par: List[EditTextField], buttons_par: List[Button],
                 images_par: List[Image], route_par, type_par):

        super().__init__(ord_par, texts_par, edits_par, buttons_par, images_par)
        UIClick.__init__(self, route_par, type_par)
