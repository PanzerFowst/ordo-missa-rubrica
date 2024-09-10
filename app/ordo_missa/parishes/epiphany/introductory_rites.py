# /app/ordo_missa/parishes/epiphany/introductory_rites.py

from ...utils import rubrify


def introductory_rites(num_deacons: int, num_servers: int) -> str:
    return f"""
Welcome to the Mass at The Church of the Epiphany.
{rubrify(procession(num_deacons, num_servers))}
"""


def procession(num_deacons: int, num_servers: int) -> str:

    procession_str: str = "The procession starts.  The priest"
    if num_deacons > 0:
        procession_str += ", joined by the "
        if num_deacons == 1:
            procession_str += "deacon on his right side, "
        elif num_deacons == 2:
            procession_str += "deacon of the Word and the deacon of the Eucharist on each of his sides, "
    procession_str += " processes from the back of the Church to the sanctuary."

    if num_servers > 0:

        # Internal function to determine who carries the crucifix:
        def crucifer(num_servers: int) -> str:
            if num_servers == 1:
                return "Server"
            if num_servers == 2:
                return "Second Master"
            else:
                return "Crucifer"
            # TODO: A better way to do this might be to assign names of the servers at
            # the beginning of this and then just call the variable that contains the
            # server's name...  self.crucifer = function_to_determine_crucifer_name()
            # Maybe also include whether the server is dedicated to his role or not?

        procession_str += f"""  The {"server" if num_servers > 0 else ""}{"s" if num_servers > 1 else ""}
        lead{"s" if num_servers == 1 else ""} the clergy in the procession.  The {crucifer(num_servers)} processes with
        the crucifix."""

    return procession_str
