function generateProcessionText(data, num_deacons, num_servers) {
    let processionText = data.welcome_message + "\n" + data.procession.base_message;

    // Process the deacon part
    if (num_deacons > 0) {
        processionText += "joined by the ";
        if (num_deacons === 1) {
            processionText += data.procession.deacon_part.text_options["1"];
        } else if (num_deacons === 2) {
            processionText += data.procession.deacon_part.text_options["2"];
        }
    }

    // Add the priest part
    processionText += data.procession.priest_part;

    // Process the servers part
    if (num_servers > 0) {
        let server_or_servers = num_servers === 1
            ? data.procession.servers_part.variables.server_or_servers["1"]
            : data.procession.servers_part.variables.server_or_servers["greater_than_1"];

        let lead_s = num_servers === 1
            ? data.procession.servers_part.variables.lead_s["1"]
            : data.procession.servers_part.variables.lead_s["greater_than_1"];

        let crucifer;
        if (num_servers === 1) {
            crucifer = data.procession.servers_part.variables.crucifer["1"];
        } else if (num_servers === 2) {
            crucifer = data.procession.servers_part.variables.crucifer["2"];
        } else {
            crucifer = data.procession.servers_part.variables.crucifer["default"];
        }

        processionText += data.procession.servers_part.base_text
            .replace("{server_or_servers}", server_or_servers)
            .replace("{lead_s}", lead_s)
            .replace("{crucifer}", crucifer);
    }

    return processionText;
}

// Example usage:
const num_deacons = 2;  // This could come from user input, e.g., a dropdown
const num_servers = 3;  // This could come from user input, e.g., an input box

const processionText = generateProcessionText(processionData, num_deacons, num_servers);
console.log(processionText);
