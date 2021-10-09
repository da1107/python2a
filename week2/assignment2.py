from abc import ABC, abstractclassmethod
import time

class HasWeight(ABC):
    @property
    @abstractclassmethod
    def weight(self) -> int:
        pass

class Astronaut(HasWeight):
    def __init__(self, weight: int):
        if weight < 50 or weight > 95:
            raise ValueError("unvalid weight according to NASA guidelines")
        self._weight = weight

    @property
    def weight(self) -> int:
        return self._weight


class Propellant (HasWeight):
    @property
    @abstractclassmethod
    def efficiency(self) -> int:
        pass

    @property
    @abstractclassmethod
    def emission(self) -> int:
        pass


class AmmoniumDinitramide (Propellant):
    def __init__(self, weight: int):
        if weight < 1 or weight > 200:
            raise ValueError("unvalid weight")
        self._weight = weight
    @property
    def weight(self) -> int:
        return self._weight
    @property
    def efficiency(self) -> int:
        return 3
    @property
    def emission(self) -> int:
        return 3


class Hydrazine (Propellant):
    def __init__(self, weight: int):
        if weight < 1 or weight > 200:
            raise ValueError("unvalid weight")
        self._weight = weight
    @property
    def weight(self) -> int:
        return self._weight
    @property
    def efficiency (self) -> int:
        return 10
    @property
    def emission (self) -> int:
        return 20

class Rocket (HasWeight):
    def __init__(self, initial_weight: int, max_weight: int):
        if initial_weight <= 0 or max_weight < initial_weight:
            raise ValueError("unvalid initial weight or max weight")
        self._weight = initial_weight
        self._max_weight = max_weight
        self.capacity = 0
        self.env_impact = 0
    
    @property
    def weight(self) -> int: 
        return self._weight

    @property
    def max_weight(self) -> int: 
        return self._max_weight

    def add_astronaut (self, ast: Astronaut):
        self._weight += ast.weight

    def add_propellant (self, propellant: Propellant): 
        self._weight += propellant.weight
        self.capacity += propellant.efficiency * propellant.weight
        self.env_impact += propellant.emission * propellant.weight
        
    
    def launch (self):
        if self._weight <= self.max_weight and self.capacity >= self._weight:
            print(f"A launch is successful. The enviroment impact is {self.env_impact}.")
        else:
            print("Someting wrong in the initial setting or Propellant weight mix is wrong")



# Help method to get the mix propellant in order to get the minimum environment impact    
def get_proposed_mixPropellant (rocket, ammoniumDinitramide, hydrazine):
    # find the minimum environmental impact when a rocket can launch successfully, and what propellant mix gives this minimum

    eff_ADN = ammoniumDinitramide.efficiency
    eff_N2H4 = hydrazine.efficiency
    emission_ADN = ammoniumDinitramide.emission
    emission_N2H4 = hydrazine.emission
    env_impact = []
    weight_mix = []

    # Each propellant weight should be more than 1 and less or equal to (rocket's max weight - rocket's weight), and
    # The mixed propellant's capacity should >= the rocket's weight.   

    max_propellant_weight = rocket.max_weight - rocket.weight
    
    for ADN in range(1, max_propellant_weight):
        for N2H4 in range(1, max_propellant_weight - ADN):
            capacity = ADN * eff_ADN + N2H4 * eff_N2H4
            if capacity >= rocket.weight + ADN + N2H4:
                env_impact.append (ADN * emission_ADN + N2H4 * emission_N2H4)
                weight_mix.append ([ADN, N2H4])
    min_impact = min (env_impact)
    index_of_best_weight_mix = env_impact.index (min_impact)
    proposed_weight_mix = weight_mix[index_of_best_weight_mix]
    print(f"The minimum environment impact is: {min_impact}, and the mixed weight is {proposed_weight_mix}.")

def create_rocket(astronauts):
    rocket = Rocket(500, 1000)
    for a in astronauts:
        rocket.add_astronaut(a)

    return rocket



def main():
    # Scenario 1: A rocket has initial weight 500 and max weight 1000, a group of astronauts weight 320, what propellant mix gives minimum enviroment impact
    print("Astronauts total weight 320 kg:")
    rocket = create_rocket([Astronaut(80) for _ in range(4)])
    
    ADN = AmmoniumDinitramide(1) # create a propellant object with an initial weight guess (this weight value is not used actually)
    N2H4 = Hydrazine(1)

    get_proposed_mixPropellant(rocket, ADN, N2H4)
    
    ADN = AmmoniumDinitramide(113) # create the propellant object with the proposed weight mix. 
    N2H4 =  Hydrazine(66)

    rocket.add_propellant(ADN)
    rocket.add_propellant(N2H4)

    rocket.launch()


    # Scenario 2: Some astronauts get nervours and eat food to calm down before launch, so the astronuants' weight are 350 now, 
    # how does this affect the mix weight of propellant to get the minimum environment impact. 
    print ("Scenarion 2: Astronuants total weight 350 kg:")
    rocket = create_rocket([Astronaut(86 + i) for i in range(4)])
    get_proposed_mixPropellant(rocket, ADN, N2H4)

    ADN = AmmoniumDinitramide(70) # create the propellant object with new proposed weight mix. 
    N2H4 =  Hydrazine(79)

    rocket.add_propellant(ADN)
    rocket.add_propellant(N2H4)

    rocket.launch()

if __name__ == "__main__":
    main()




        










