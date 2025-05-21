# python-OOP-Lec4-21-MAY-25
* all dunder functions come from the super class Object.
  * therefore when we override these functions need to add the metadata @override and import it:
    * from typing import override
* shortcut: @props will create getter and setters
* if we want to use the protection of the getters and setters in the init function better to call the setter:
  * self.radius=_radius
  * same every when want to set/get the private property:
    * instead self.__radius, use self.radius , because it calls the setter/getter functions
* can create @property for parameter, even if it's not attribute in the class.
  * this is instead to call function, call the "property":
    * instead function def get_area(self)=> create @property def area(self)
    * then we can access the area property: c1.area
* static:
  *  static parameter will be a part of the class and not part of the object,
  * it will be defined 1 time in the class and not for each instance!
  ```
  class Circle:
    pie=3.14
    def __init__(self):....
  ```
  * to access it : Circle.pie
  * can be private to public, with __pie and getter/setter
  * if it's private, can be access only within the class and not outside it.