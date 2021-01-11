from element import element
import math

"""
Creates Periodic Table with 72 of 118 elements, and handles calculation methods.
"""

table = []

table.append(element('Hydrogen', 'H', 'Reactive Nonmetals', 1, 1.008))
table.append(element('Helium', 'He', 'Noble Gases', 2, 4.0026))
table.append(element('Lithium', 'Li', 'Alkali Metals', 3, 6.94))
table.append(element('Beryllium', 'Be', 'Alkaline Earth Metals', 4, 9.0122))
table.append(element('Boron', 'B', 'Metalloids', 5, 10.81))
table.append(element('Carbon', 'C', 'Reactive Nonmetals', 6, 12.011))
table.append(element('Nitrogen', 'N', 'Reactive Nonmetals', 7, 14.007))
table.append(element('Oxygen', 'O', 'Reactive Nonmetals', 8, 15.999))
table.append(element('Fluorine', 'F', 'Reactive Nonmetals', 9, 18.998))
table.append(element('Neon', 'Ne', 'Noble Gases', 10, 20.180))
table.append(element('Sodium', 'Na', 'Alkali Metals', 11, 22.990))
table.append(element('Magnesium', 'Mg', 'Alkaline Earth Metals', 12, 24.305))
table.append(element('Aluminum', 'Al', 'Post-Transition Metals', 13, 26.982))
table.append(element('Silicon', 'Si', 'Metalloids', 14, 28.085))
table.append(element('Phosphorus', 'P', 'Reactive Nonmetals', 15, 30.974))
table.append(element('Sulfur', 'S', 'Reactive Nonmetals', 16, 32.06))
table.append(element('Chlorine', 'Cl', 'Reactive Nonmetals', 17, 35.45))
table.append(element('Argon', 'Ar', 'Noble Gases', 18, 39.948))
table.append(element('Potassium', 'K', 'Alkali Metals', 19, 39.098))
table.append(element('Calcium', 'Ca', 'Alkaline Earth Metals', 20, 40.078))
table.append(element('Scandium', 'Sc', 'Transition Metals', 21, 44.956))
table.append(element('Titanium', 'Ti', 'Transition Metals', 22, 47.867))
table.append(element('Vanadium', 'V', 'Transition Metals', 23, 50.942))
table.append(element('Chromium', 'Cr', 'Transition Metals', 24, 51.996))
table.append(element('Manganese', 'Mn', 'Transition Metals', 25, 54.938))
table.append(element('Iron', 'Fe', 'Transition Metals', 26, 55.845))
table.append(element('Cobalt', 'Co', 'Transition Metals', 27, 58.933))
table.append(element('Nickel', 'Ni', 'Transition Metals', 28, 58.693))
table.append(element('Copper', 'Cu', 'Transition Metals', 29, 63.546))
table.append(element('Zinc', 'Zn', 'Transition Metals', 30, 65.38))
table.append(element('Gallium', 'Ga', 'Post-Transition Metals', 31, 69.723))
table.append(element('Germanium', 'Ge', 'Metalloids', 32, 72.630))
table.append(element('Arsenic', 'As', 'Metalloids', 33, 74.922))
table.append(element('Selenium', 'Se', 'Reactive Nonmetals', 34, 78.971))
table.append(element('Bromine', 'Br', 'Reactive Nonmetals', 35, 79.904))
table.append(element('Krypton', 'Kr', 'Noble Gases', 36, 83.798))
table.append(element('Rubidium', 'Rb', 'Alkali Metals', 37, 85.468))
table.append(element('Strontium', 'Sr', 'Alkaline Earth Metals', 38, 87.62))
table.append(element('Yttrium', 'Y', 'Transition Metals', 39, 88.906))
table.append(element('Zirconium', 'Zr', 'Transition Metals', 40, 91.224))
table.append(element('Niobium', 'Nb', 'Transition Metals', 41, 92.906))
table.append(element('Molybdenum', 'Mo', 'Transition Metals', 42, 95.95))
table.append(element('Technetium', 'Tc', 'Transition Metals', 43, 98))
table.append(element('Ruthenium', 'Ru', 'Transition Metals', 44, 101.47))
table.append(element('Rhodium', 'Rh', 'Transition Metals', 45, 102.91))
table.append(element('Palladium', 'Pd', 'Transition Metals', 46, 106.42))
table.append(element('Silver', 'Ag', 'Transition Metals', 47, 107.87))
table.append(element('Cadmium', 'Cd', 'Transition Metals', 48, 112.41))
table.append(element('Indium', 'In', 'Post-Transition Metals', 49, 114.82))
table.append(element('Tin', 'Sn', 'Post-Transition Metals', 50, 118.71))
table.append(element('Antimony', 'Sb', 'Metalloids', 51, 121.76))
table.append(element('Tellurium', 'Te', 'Metalloids', 52, 127.60))
table.append(element('Iodine', 'I', 'Reactive Nonmetals', 53, 126.90))
table.append(element('Xenon', 'Xe', 'Noble Gases', 54, 131.29))
table.append(element('Caesium', 'Cs', 'Alkali Metals', 55, 132.91))
table.append(element('Barium', 'Ba', 'Alkaline Earth Metals', 56, 137.33))
# 57-71
table.append(element('Hafnium', 'Hf', 'Transition Metals', 72, 178.49))
table.append(element('Tantlum', 'Ta', 'Transition Metals', 73, 180.95))
table.append(element('Tungsten', 'W', 'Transition Metals', 74, 183.84))
table.append(element('Rhenium', 'Re', 'Transition Metals', 75, 186.21))
table.append(element('Osmium', 'Os', 'Transition Metals', 76, 190.23))
table.append(element('Iridium', 'Ir', 'Transition Metals', 77, 192.22))
table.append(element('Platinum', 'Pt', 'Transition Metals', 78, 195.08))
table.append(element('Gold', 'Au', 'Transition Metals', 79, 196.97))
table.append(element('Mercury', 'Hg', 'Transition Metals', 80, 200.59))
table.append(element('Thallium', 'Tl', 'Post-Transition Metals', 81, 204.38))
table.append(element('Lead', 'Pb', 'Post-Transition Metals', 82, 207.2))
table.append(element('Bismuth', 'Bi', 'Post-Transition Metals', 83, 208.98))
table.append(element('Polonium', 'Po', 'Post-Transition Metals', 84, 209))
table.append(element('Astatine', 'At', 'Metalloids', 85, 210))
table.append(element('Radon', 'Rn', 'Noble Gases', 86, 222))
table.append(element('Francium', 'Fr', 'Alkali Metals', 87, 223))
table.append(element('Radium', 'Ra', 'Alkaline Earth Metals', 88, 226))
# 89-103
# 104-118


def getSymbol(number):
    """
    Method to get a symbol from the Periodic Table based on atomic number.

    Parameters
    ----------
    number : int
        The atomic number of the element being searched.

    Returns
    ----------
    sym : str
        The symbol of the element searched.
    """
    sym = table[(number - 1)].symbol
    return sym

def searchElement(attr):
    """
    Method to search for element on periodic table from either name, symbol, atomic number, or atomic weight.

    Parameters
    ----------
    attr : str
        A String attribute of the element (name, symbol, atomic number, or atomic weight).
    
    Returns
    ----------
    element : Element
        The Element object of the element being searched, if found.
    """
    for element in table:
        if element.name == attr:
            return element
        elif element.symbol == attr:
            return element
        elif str(element.number) == attr:
            return element
        elif str(element.weight) == attr:
            return element
    
    return None
    
def getMolecularWeight(compound):
    """
    Method that calculates molecular weight based on compound.

    Parameters
    ----------
    compound : str
        The compound of elements, in symbols. Example: H2O = "HHO"
    
    Returns
    --------
    mw : double
        The molecular weight of the compound.
    """

    symbols = []

    for x in compound:
        if x.isupper(): # if upper case
            if compound.index(x) == len(compound)-1: # if last index
                symbols.append(x)
            else: # if not last index
                y = compound.index(x) + 1
                if compound[y].islower():
                    symbols.append(x + compound[y])
                else: # if next index is upper case
                    symbols.append(x)
    
    mw = 0
    for x in symbols:
        for y in table:
            if x == y.symbol:
                mw = mw + y.weight
    
    mw = '{0:.8g}'.format(mw)
    return mw

def getMol(compound, grams):
    """
    Method that calculates the molecular weight based on compound and amount (grams).

    Parameters
    ----------
    compound : str
        The compound of elements, in symbols. Example: H2O = "HHO"

    grams : double
        The amount of grams given.

    Returns
    ----------
    mc : double
        The molecular weight of the compound based on amount given.
    """
    mw = '{0:.8f}'.format(getMolecularWeight(compound))
    mc = '{0:.8f}'.format((mw * grams))
    
    return mc

def getHalfLife(massI, massF, time, halflife, rate):
    """
    Method that performs half-life equations. User inputs 0 for unknown variable of interest, 1 for other unknown variables.

    Parameters:
    massI : double
        The initial mass given.
    
    massF : double
        The final mass.
    
    time : double
        The time duration of the reaction.

    halflife : double
        The half-life of the element.

    rate : double
        The rate constant of the reaction.

    Returns
    ----------
    result : str
        The result of the half-life equation, returns variable of interest.
    """
    # Solving for initial mass (does not account for rate==1)
    if massI == 0:
        massI = massF / math.pow(math.e, -rate*time)
        result = "Initial Mass: " + str(massI)

    # Solving for final mass
    elif massF == 0:
        if massI == 1: # if unknown massI
            power = '{0:.5g}'.format(time/halflife)
            massF = '{0:.5g}'.format(100/math.pow(2, power))
        else:
            x = time/halflife # x = amount of half lives
            massF = massI * (math.pow(0.5, x))
        result = "Final Mass: " + str(massF)
    
    # Solving for time duration
    elif time == 0:
        time = halflife * math.log((massF/massI), 0.5)
        result = "Time: " + str(time)

    # Solving for half-life
    elif halflife == 0:
        if massI == 1 and massF == 1 and time == 1:
            halflife = 0.693/rate
        else:
            n = math.log((massF/massI), 0.5)
            halflife = time/n
        result = "Half-Life: " + str(halflife)
    
    # Solving for rate
    elif rate == 0:
        if massI == 1 and massF == 1 and time == 1:
            rate = 0.693/halflife
        else:
            rate = '{0:.5g}'.format((-1/time) * (math.log10((massF/massI))))
        result = "Rate: " + str(rate)
    
    else:
        result = "Error."

    return result

def getNuclearDecay(mass, number, decay):
    """
    Method to perform nuclear decay equations.

    Parameters
    ----------
    mass : int
        The atomic mass of the element.

    number : int 
        The atomic number of the element.

    decay : str
        The type of nuclear decay.

    Returns
    ----------
    daughter : str
        The resulting daughter from the nuclear fission equation.
    """
    if decay.islower() == "alpha".islower(): # Alpha Decay
        daughter = "Daughter: " + str(mass-4) + ";" + str(number-2) + " " + getSymbol(number, -2)
    elif decay.islower() == "beta".islower(): # Beta Decay
        daughter = "Daughter: " + str(mass) + ";" + str(number+1) + " " + getSymbol(number, 1)
    elif decay.islower() == "positron".islower(): # Positron Emission
        daughter = "Daughter: " + str(mass) + ";" + str(number-1) + " " + getSymbol(number, -1)
    elif decay.islower() == "electron".islower(): # Electron Transfer
        daughter = "Daughter: " + str(mass) + ";" + str(number+1) + " " + getSymbol(number, 1)
    elif decay.islower() == "gamma".islower(): # Gamma Decay
        daughter = "Daughter: " + str(mass) + ";" + str(number) + getSymbol(number, 0) + " + 0/0γ"    
    else:
        daughter = "Error."

    return daughter

def getNuclearFission(mol):
    """
    Method to calculate nuclear fission by mol.

    Parameters
    ----------
    mol : double
        The number of mol given.

    Returns
    ----------
    nuclearFission : double
        The nuclear fission constant.

    power : int
        The power of the nuclear fission constant.
    """
    energy = 1.6 # total energy per U-235 atom
    powerE = -13 # exp of total energy per U-235 atom
    avo = 6.022 # avogadro's mol number
    powerA = 23 # exp of avogadro's mol number

    nuclearFission = energy * avo * mol
    power = powerE + powerA

    return nuclearFission, power
