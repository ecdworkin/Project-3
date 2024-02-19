
// Use d3 to read the JSON file.
// The data from the JSON file is arbitrarily named importedData as the argument.
d3.json("http://localhost:8000/crime_data.json").then((importedData) => {

    // Create the tile layer that will be the background of our map.
    let streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });

    // Initialize Leaflet map
    var map =  L.map("map-id", {
        center: [36.1716, -115.1391],
        zoom: 13
    });

    streetmap.addTo(map);

    var pointCounts = {};
    importedData.forEach(point => {
        point["incidents"].forEach(incident => {
            var latLng = [incident.incident_latitude, incident.incident_longitude];
            var key = latLng.join(',');
            pointCounts[key] = (pointCounts[key] || 0) + 1;
        })
    });

    // Convert aggregated data into heatmap format
    var heatmapData = [];
    for (var key in pointCounts) {
        var latLng = key.split(',').map(Number);
        heatmapData.push([latLng[0], latLng[1], pointCounts[key]]);
    }
    // Create heatmap layer
    L.heatLayer(heatmapData, { radius: 25 }).addTo(map);
})

