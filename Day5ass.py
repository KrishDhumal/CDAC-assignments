#Question 1
"""
class Grandparent {
    Grandparent() {
        System.out.println("Grandparent constructor");
    }
}

class Parent extends Grandparent {
    Parent() {
        super();
        System.out.println("Parent constructor");
    }
}

class Child extends Parent {
    Child() {
        super();
        System.out.println("Child constructor");
    }
}

public class Main1 {
    public static void main(String[] args) {
        Child c = new Child();
    }
}
"""

#Question 2
"""
class Vehicle {
    public void start() {
        System.out.println("Vehicle is starting");
    }
}

class FourWheeler extends Vehicle {
    @Override
    public void start() {
        System.out.println("Four Wheeler is starting");
    }

    public static void main(String[] args) {
        FourWheeler car = new FourWheeler();
        car.start();
    }
}
"""

#Question 3
"""
class Animal {
    Animal() {
        System.out.println("Animal constructor");
    }
}

class Dog extends Animal {
    Dog() {
        System.out.println("Dog constructor");
    }
}

class Cat extends Animal {
    Cat() {
        System.out.println("Cat constructor");
    }
}

public class Main3 {
    public static void main(String[] args) {
        Dog d = new Dog();
        Cat c = new Cat();
    }
}
"""

#Question 4
"""
class Top1 {
    void disp1() {
        System.out.println("Top1 display");
    }
}

class Bottom1 extends Top1 {
    @Override
    void disp1() {
        System.out.println("Bottom1 display");
    }
}

class Bottom2 extends Top1 {
    @Override
    void disp1() {
        System.out.println("Bottom2 display");
    }
}

class Bottom3 extends Top1 {
    @Override
    void disp1() {
        System.out.println("Bottom3 display");
    }
}

public class Main4 {
    static void perform(Top1 t) {
        t.disp1();
    }

    public static void main(String[] args) {
        perform(new Bottom1());
        perform(new Bottom2());
        perform(new Bottom3());
    }
}
"""

#Question 5
"""
class Base {
    Base(String msg) {
        System.out.println("Base class constructor: " + msg);
    }
}

class Sub extends Base {
    Sub(String msg) {
        super(msg);
        System.out.println("Sub class constructor: " + msg);
    }

    public static void main(String[] args) {
        Sub s = new Sub("Hello Java");
    }
}
"""
#Exception handling

"""
class VotingNotAllowedException(Exception):
    def __init__(self, message="Age is less than 18. Voting not allowed."):
        super().__init__(message)


class Voter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if age < 18:
            raise VotingNotAllowedException(f"{name} is not eligible to vote. Age: {age}")
        else:
            print(f"{name} is eligible to vote. Age: {age}")
"""
#Question 3
"""
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    person = Voter(name, age)
except VotingNotAllowedException as e:
    print("Exception caught:", e)
"""
