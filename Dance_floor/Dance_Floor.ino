# define trig 2
# define echo 3
# define trig1 4
# define echo1 5
# define trig2 6
# define echo2 7
# define trig3 8
# define echo3 9
# define trig4 10
# define echo4 11
//#define led1 36
//#define led2 37
//#define led3 38
//#define led4 39


//# define trig5 12
//# define echo5 13
void setup() {
 
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  pinMode(trig1,OUTPUT);
  pinMode(echo1,INPUT);
  pinMode(trig2,OUTPUT);
  pinMode(echo2,INPUT);
  pinMode(trig3,OUTPUT);
  pinMode(echo3,INPUT);
//  pinMode(trig4,OUTPUT);
//  pinMode(echo4,INPUT);
//  pinMode(trig5,OUTPUT);
//  pinMode(echo5,INPUT);
  Serial.begin(9600);
//  pinMode(40,OUTPUT);
//  pinMode(42,OUTPUT);
}

void loop() {

   pinMode(40,LOW);
  pinMode(42,HIGH);
  digitalWrite(trig,LOW);
  delay(2);
  digitalWrite(trig,HIGH);
  delay(10);
  digitalWrite(trig,LOW);
  int a= pulseIn(echo,HIGH);
  a/=100;
  String str2,str1;
//  Serial.println(a);
  if(a<0){
   a=200;
  }
  str1= String(a);
    
  digitalWrite(trig1,LOW);
  delay(2);
  digitalWrite(trig1,HIGH);
  delay(10);
  digitalWrite(trig1,LOW);
  int b= pulseIn(echo1,HIGH);
  b/=100;
  if(b<0){
  b=200;}
  str2= String(b);  
  
//    digitalWrite(trig2,LOW);
//    delay(2);
//    digitalWrite(trig2,HIGH);
//    delay(10);
//    digitalWrite(trig2,LOW);
//    int c= pulseIn(echo2,HIGH);
//    c/=100;
//   // Serial.println(c);
//   // String str3;
//    if (c<0)
   int c=200;
String str3= String(c);

  
  
  
    digitalWrite(trig3,LOW);
    delay(2);
    digitalWrite(trig3,HIGH);
    delay(10);
    digitalWrite(trig3,LOW);
    int d= pulseIn(echo3,HIGH);
    d/=100;
  //  Serial.println(d);
    if (d<0)
    d=200;
   String str4= String(d);
//  
//  
//  
//    digitalWrite(trig4,LOW);
//    delay(2);
//    digitalWrite(trig4,HIGH);
//    delay(10);
//    digitalWrite(trig4,LOW);
//    int e= pulseIn(echo4,HIGH);
//    e/=100;
//    String str5= String(e);
  
  
  
 //   digitalWrite(trig5,LOW);
//    delay(2);
//    digitalWrite(trig5,HIGH);
//    delay(10);
//    digitalWrite(trig5,LOW);
//    int f= pulseIn(echo5,HIGH);
//    f/=100;
//    Serial.println(f);
//    String str6= String(f);
//  
//    String str = str1+"+"+str2+"-"+str3+"*"+str4+"="+str5+"/"+str6;

//      String str5 = String(0);
      
      String str = str1+"+"+str2+"-"+str3+"*"+str4;
  //    if(a>0 && b>0)
      Serial.println(str);

  
}
