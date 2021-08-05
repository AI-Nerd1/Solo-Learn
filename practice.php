$a=2; $b=$a++;
echo $b

<form action="first.php" method="post">
  <p>Name: <input type="text" name="name" /></p>
  <p>Age: <input type="text" name="age" /></p>
  <p><input type="submit" name="submit" value="Submit" /></p>
</form>

<html>
<body>

Welcome <?php echo $_POST["name"]; ?><br />
Your age: <?php echo $_POST["age"]; ?>

</body>
</html>

<form action="actionGet.php" method="get">
  Name: <input type="text" name="name" /><br /><br />
  Age: <input type="text" name="age" /><br /><br />
  <input type="submit" name="submit" value="Submit" />
</form>

<?php
echo "Hi ".$_GET['name'].". ";
echo "You are ".$_GET['age']." years old.";
?>


<?php
// Start the session
session_start();

$_SESSION['color'] = "red";
$_SESSION['name'] = "John";
?>

<?php
// Start the session
session_start();
?>
<!DOCTYPE html>
<html>
<body>
<?php
echo "Your name is " . $_SESSION['name'];
// Outputs "Your name is John"
?>
</body>
</html>

$myfile = fopen("file.txt", "w");
PHP


<?php
$myfile = fopen("names.txt", "w");

$txt = "John\n";
fwrite($myfile, $txt);
$txt = "David\n";
fwrite($myfile, $txt);

fclose($myfile);

/* File contains:
John
David
*/
?>

$myFile = "test.txt";
$fh = fopen($myFile, 'a');
fwrite($fh, "Some text");
fclose($fh);

<?php
if(isset($_POST['text'])) {
  $name = $_POST['text'];
  $handle = fopen('names.txt', 'a');
  fwrite($handle, $name."\n");
  fclose($handle); 
}
?>
<form method="post">
  Name: <input type="text" name="text" /> 
  <input type="submit" name="submit" />
</form>

class Person {
  public $age; //property
  public function speak() { //method
    echo "Hi!"
  }
}

<?php
class Person {
    public $age;
    function speak() {
        echo "Hi!";
    }
}
$p1 = new Person(); 
$p1->age = 23;
echo $p1->age; 
$p1->speak();
?>

<?php
class Dog {
    public $legs=4;
    public function display() {
        echo $this->legs;
    }
}
$d1 = new Dog();
$d1->display();

echo '<br />';

$d2 = new Dog();
$d2->legs = 2;
$d2->display();
?>

<?php
abstract class Fruit { 
    private $color; 
    
    abstract public function eat(); 
    
    public function setColor($c) { 
        $this->color = $c; 
    } 
} 

class Apple extends Fruit {
    public function eat() {
        echo "Omnomnom";
    }
}

$obj = new Apple();
$obj->eat();
?>