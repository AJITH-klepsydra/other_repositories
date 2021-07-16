# define trig 9
# define echo 10
# define trig1 5
# define echo1 4
# define echo2 6
# define trig2 7

void setup ()
{
  pinMode(echo2, INPUT);
  pinMode(trig2, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  pinMode(echo1, INPUT);
  pinMode(trig1, OUTPUT);
  Serial.begin(9600);
}
void loop ()
{
  digitalWrite(trig,LOW);
  delay(2);
  digitalWrite(trig,HIGH);
  delay(10);
  digitalWrite(trig,LOW);
  int b= pulseIn(echo,HIGH);
  b/=100;
  String s1 = String(b);
// Serial.println(s1);
 digitalWrite(trig1,LOW);
  delay(2);
  digitalWrite(trig1,HIGH);
  delay(10);
  digitalWrite(trig1,LOW);
  int c= pulseIn(echo1,HIGH);
  c/=100;
  String s2 = String(c);
// Serial.println(c);

digitalWrite(trig2,LOW);
  delay(2);
  digitalWrite(trig2,HIGH);
  delay(10);
  digitalWrite(trig2,LOW);
  int d= pulseIn(echo2,HIGH);
  d/=100;
  String s3 = String(c);
// Serial.println(c);
String s4 = String(s1+"+"+s2+"-"+s3);
Serial.println(s4H);
delay(200);
}
