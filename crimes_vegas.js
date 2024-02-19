// Initialize Leaflet map
var map = L.map('map').setView([0, 0], 2);
  
  // Add a tile layer.
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

// Use d3 to read the JSON file.
// The data from the JSON file is arbitrarily named importedData as the argument.
d3.json("crimedata.json").then((importedData) => {
    // console.log(importedData);
    let data = importedData;

})

 // Process the data to aggregate points
    var pointCounts = {};
    data.forEach(point => {
    var latLng = [point.latitude, point.longitude];
        var key = latLng.join(',');
        pointCounts[key] = (pointCounts[key] || 0) + 1;

    });

    // Convert aggregated data into heatmap format
    var heatmapData = [];
    for (var key in pointCounts) {
        var latLng = key.split(',').map(Number);
        heatmapData.push([latLng[0], latLng[1], pointCounts[key]]);
    }

    // Create heatmap layer
    var heat = L.heatLayer(heatmapData, { radius: 25 }).addTo(map);
