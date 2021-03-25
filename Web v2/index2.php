<!DOCTYPE html>
<html lang="fr">

  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" type="image/x-icon" href="image/SN.png">
    <link rel="stylesheet" type="text/css" href="style.css">
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
    <title>CHAUFFE-EAU CONNECTE</title>
  </head>

<body>
  <header>
    <p class="Titre">CHAUFFE-EAU CONNECTE</p>
  </header>

  <nav>
      <input type="checkbox" id="check">
      <label for="check" class="checkbtn">
          <i class="fas fa-bars"></i>
      </label>
      <ul>
        <li><a href="index.html">Accueil</a></li>
        <li><a class="active" href="#">Contrôle</a></li>  
      </ul>
    </nav>

    <section>
        <div class="artitre">
            <p>Contrôle chauffe-eau</p>
        </div>
        <form action="script.php" method="post">
            <input type="submit" name="executer" value="ON" class="button" id="ON">
            <br/>
            <input type="submit" name="executer" value="OFF" class="buttoff" id="OFF">
        </form>
    </section>

</body>
</html>