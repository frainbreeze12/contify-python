TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="shortcut icon" type="image/x-icon" href="assets/img/favicon.ico">
  <title>Contify</title>
  <!-- Compiled and minified CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <nav class="blue darken-2">
    <div class="nav-wrapper space">
      <a href="#" class="brand-logo"><img src="assets/img/logo-white.png" class="logo-img"></a>
      <ul id="nav-mobile" class="right hide-on-med-and-down">
        <li>Letzte Aktualisierung: {{VAR_TIME}}</li>
      </ul>
    </div>
  </nav>

<main>
<div  class="row">
{{VAR_LINKS}}
</div>
</main>

<footer class="page-footer blue darken-2">
  <div class="row space">
    <span class="col-s-4">© 2019 Copyright Text</span>
    <a class="grey-text text-lighten-4 right" href="#!">More Links</a>
  </div>
</footer>

<!-- Compiled and minified JavaScript -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</body>
</html>
"""
