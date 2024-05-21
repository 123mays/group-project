<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="/static/example.css">
  <script src="/static/example.js"></script>
</head>
<body>
  <h1 class="my-class" id="hello">USA Chronic Disease Indicator</h1>
  <p>
    <label for="Year">Select Year:</label> 
    <select name="Year" id="Year">
      {{ YearOptions|safe }}
    </select>

    <label for="Age">Select Age:</label> 
    <select name="Age" id="Age">
      {{ AgeOptions|safe }}
    </select>

    <label for="Disease">Select Disease:</label> 
    <select name="Disease" id="Disease">
      {{ DiseaseOptions|safe }}
    </select>

    <!-- Add other dropdowns similarly -->
  </p>
  <button class="big-button" onclick="addDropdownItem()">Enter</button>
</body>
</html>
