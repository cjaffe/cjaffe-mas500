var width = 1300,
    height = 850;

var points = []; 

var sortedPoints, shortSortedPoints;
var potholeCount, roadQuality;

var svg = d3.select( "#map" )
  .append( "svg" )
  .attr( "width", width )
  .attr( "height", height );

var g = svg.append( "g" );
var g2 = svg.append( "g" );
var g3 = svg.append( "g" );

/* Initialize tooltip */
var tip = d3.tip().attr('class', 'd3-tip').html(function(d) { 
  var imuVal = d.imu1 + d.imu2;
  return "<p>Road Quality Index: " + d.value;
});

/* Invoke the tip in the context of your visualization */
g3.call(tip);

var albersProjection = d3.geo.albers()
  .scale( 800000 )
  .rotate( [71.057,0] )
  .center( [-0.06, 42.375477] )
  .translate( [width/2,height/2] );

var geoPath = d3.geo.path()
    .projection( albersProjection );

//draw neighborhoods
g.selectAll( "path" )
  .data( neighborhoods_json.features )
  .enter()
  .append( "path" )
  .attr( "fill", "#e5f5f9")//"#fee5d9" )
  .attr( "d", geoPath );

var streets = streets_json.features;
var sortedStreets = streets.sort( function(a,b) 
    { return b.id > a.id; }
  );

// give fake data values to each point
sortedStreets.map(function(d) {
  d.geometry.coordinates.map(function(d) {
    d.value = Math.floor((10*Math.random()* 100) / 100);
  });
});

//draw streets
g2.selectAll( "path" )
  .data( sortedStreets )
  .enter()
  .append( "path" )
  .attr( "stroke", "#99d8c9")//"#fcbba1")
  .attr("stroke-width", 2)
  .attr("fill", "none")
  .attr( "d", geoPath )
  .on("click", function(d) {
    showStreetData(d);
  });

//draw second set of clear/ fat streets
g3.selectAll( "path" )
  .data( sortedStreets )
  .enter()
  .append( "path" )
  .attr( "stroke", "#99d8c9")//"#fcbba1")
  .attr("stroke-width", 7)
  .attr("fill", "none")
  .attr("opacity", 0)
  .attr( "d", geoPath )
  .on("click", function(d) {
    showStreetData(d);
  });



function getThisStreet(id) {
  return streets.filter(function(d) {
    return d.properties.Street_ID === id;
  });
}

// get points for street with certain ID
function getThisStreetShortSortedPoints(streetSegments) {
  //console.log(streetSegments);
  streetSegments.map(function(d) {
      points = points.concat(d.geometry.coordinates);

      sortedPoints = points.sort( function(a,b) { return a[1] - b[1]; });
      shortSortedPoints = sortedPoints.filter(function(d, i) { return i%4 === 0; });
    });
}

function showStreetData(d) {
  console.log(d.properties.Street_ID);
  removeCurrentMapData();
  points = [];
  sortedPoints = [];
  shortSortedPoints = [];
  getThisStreetShortSortedPoints(getThisStreet(d.properties.Street_ID)); //puts points into shortSortedPoints
  //console.log(shortSortedPoints.length);
  updateMap();
  potholeCount = shortSortedPoints.reduce(function(result, arr) {
    if (arr.value === 1 || arr.value === 0) {
      return result += 1;
    } else {
      return result; 
    }
  }, 0);

  roadQuality = shortSortedPoints.reduce(function(result, arr) {
    return result += arr.value;
  }, 0);

  roadQuality = (roadQuality)/ shortSortedPoints.length;


  $("#data").html("<p>Street Name: " + d.properties.Label + 
      "</p><p>Number of Potholes: " + potholeCount +
      "</p><p>Road Safety Index: " + roadQuality + "</p>"
  );
  $("#tab-data").show();
}

function clearData() {
  $("#tab-data").hide();
}

function removeCurrentMapData() {
  g3.selectAll("circle")
  .remove();
 }

function updateMap() {
  g3.selectAll("circle")
	.data(shortSortedPoints)
	.enter()
	.append("circle")
  //.transition()
  //.delay(function (d, i) { return (i+1)*50;})
	.attr("cx", function (d) { //console.log(d); 
    return albersProjection(d)[0]; })
	.attr("cy", function (d) { return albersProjection(d)[1]; })
	.attr("r", "4px")
	.attr("fill", function(d) { 
    if (d.value < 10) { return "#a50f15"; }
    else if (d.value < 50) { return "#de2d26"; }
    else if (d.value < 100) { return "#fb6a4a"; }
    else { return "#fc9272"; } })
  .on('mouseover', tip.show)
  .on('mouseout', tip.hide);
}