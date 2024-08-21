# /app/ordo_missa/parishes/st_agnes/mass_text.py

from ordo_missa.ordo_missa_abc import OrdoMissaABC


class StAgnes(OrdoMissaABC):

    def introductory_rites(self) -> str:
        return """Welcome to the Mass at The Church of St. Agnes. Introductory Rites...
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

    def liturgy_of_the_word(self) -> str:
        return f"""Liturgy of the Word for St. Agnes... {
            generate_mass_text(
                self.num_deacons)}
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

    def liturgy_of_the_eucharist(self) -> str:
        return """Liturgy of the Eucharist for St. Agnes...
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

    def communion_rite(self) -> str:
        return """Communion Rite for St. Agnes...
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

    def concluding_rites(self) -> str:
        return """Concluding Rites for St. Agnes.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


def generate_mass_text(num_deacons: int) -> str:
    if num_deacons == 0:
        return "The priest reads the Gospel at St. Agnes."
    elif num_deacons == 1:
        return "The deacon reads the Gospel at St. Agnes."
    elif num_deacons == 2:
        return "The deacon of the Word reads the Gospel at St. Agnes."
    else:
        raise Exception(f"Invalid number of deacons: {num_deacons}")
