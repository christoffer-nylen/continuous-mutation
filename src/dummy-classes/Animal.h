#ifndef ANIMAL_H
#define ANIMAL_H

class Animal {
public:
  virtual void cry() = 0;
  virtual int getNumberOfLegs() = 0;
};

#endif /* ANIMAL_H */
