String otherName = "";
String displayed ="";
String displayed2 ="";
String lines[];
int index;
int i;

int interval = 12; // 2s
int time;

PFont font;

void setup() {
  fullScreen();
  font = createFont("arial", 56);
  background(0);
  displayed = "";
  displayed2 = "";
  time = millis();
  textFont(font);
  fill(0, 0, 0);
  String lines[] = loadStrings("/home/pi/med_names1.txt");
  println("there are " + lines.length + " lines");
}

void draw() {
  background(255, 255, 255);
  text(displayed, width/2 - textWidth(displayed)/2, height/2);
  String lines[] = loadStrings("/home/pi/med_names1.txt");
  int index = int(random(lines.length));
  if (lines.length > 0){
  if (millis() - time > interval) {
      displayed = displayed.equals(lines[1000])? otherName:lines[1000];
      time  = millis() + millis()/2;   
  }
  else if (index > 2400){ 
      int nu = index;
      displayed = displayed.equals(lines[nu])? otherName:lines[nu];
      time  = millis();
      print(nu);
    }
  }
  else {
    displayed = " WAIT / READ / WRITE  ";
  }
  
 
}
