from uiElements.UiElement import UIElement
from uiElements.UIClick import UIClick


class Button(UIElement, UIClick):
    def __init__(self, ord_par, text_par, route_par, type_par, route_navigation_par):
        super().__init__(ord_par)
        UIClick.__init__(self, route_par, type_par, route_navigation_par)
        self.text = text_par
