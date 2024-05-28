from experta import *


class SEArqueologia(KnowledgeEngine):

    @DefFacts()
    def inicial(self):
        yield Fact(start=True)

    #Funciones

    def ask_question(self, question, allowed_values):
        answer = input(question)
        answer = answer.lower()
        while answer not in allowed_values:
            answer = input(question)
            answer = answer.lower()
        return answer

    def yes_or_no(self, question):
        response = self.ask_question(question, ["si", "no", "s", "n"])
        return response in ["si", "s"]

    #Reglas

    @Rule(Fact(start=True))
    def bienvenida(self):
        respuesta = input(
            "Bienvenido al Sistema Experto de Artefactos Arqueológicos\n" + "Ingrese el material del artefacto: ").lower()
        self.declare(Fact(material=respuesta))

    @Rule(Fact(material='piedra'))
    def R1(self):
        if self.yes_or_no("¿Tiene un borde afilado? (si/no)? "):
            self.declare(Fact(afilado=True))
        else:
            self.declare(Fact(afilado=False))

    @Rule(Fact(afilado=True))
    def R2(self):
        if self.yes_or_no("¿La herramienta tiene decoraciones o inscripciones? (si/no)? "):
            self.declare(Fact(detalles=True))
        else:
            self.declare(Fact(detalles=False))

    @Rule(Fact(detalles=True))
    def R3(self):
        if self.yes_or_no("¿Las decoraciones y/o incripciones son simbolos religiosos? (si/no)? "):
            self.declare(Fact(ritual=True))
        else:
            self.declare(Fact(decorativo=True))

    @Rule(Fact(afilado=False))
    def R4(self):
        if self.yes_or_no("¿La herramienta tiene decoraciones o inscripciones? (si/no)? "):
            self.declare(Fact(detalles=True))
        else:
            self.declare(Fact(detalles=False))

    @Rule(Fact(material='piedra'), Fact(afilado=True), Fact(detalles=False))
    def R5(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de piedra, entonces es una herramienta de corte o arma  de uso recurrente como un cuchillo, un hacha o una punta de flecha.\n")

    @Rule(Fact(material='piedra'), Fact(afilado=True), Fact(detalles=True), Fact(ritual=True))
    def R6(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de piedra y con alguna decoración, inscripcion o simbolo religioso, entonces es una herramienta de corte o arma como un cuchillo, un hacha o una punta de flecha, el cual se usa en rituales.\n")

    @Rule(Fact(material='piedra'), Fact(afilado=True), Fact(detalles=True), Fact(decorativo=True))
    def R7(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de piedra y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una herramienta de corte o arma como un cuchillo, un hacha o una punta de flecha, el cual es un objeto decorativo o de prestigio.\n")

    @Rule(Fact(material='piedra'), Fact(afilado=False), Fact(detalles=False))
    def R8(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de piedra, entonces es una herramienta de un uso general en algun oficio como la agricultura, cocina, raspar, etc.\n")

    @Rule(Fact(material='piedra'), Fact(afilado=False), Fact(detalles=True), Fact(ritual=True))
    def R9(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de piedra y con alguna decoración, inscripcion o simbolo religioso, entonces es una herramienta de algun uso general, el cual se usa en rituales.\n")

    @Rule(Fact(material='piedra'), Fact(afilado=False), Fact(detalles=True), Fact(decorativo=True))
    def R10(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de piedra y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una herramienta de un uso general algun oficio como la agricultura, cocina, raspar, etc., el cual es un objeto decorativo o de prestigio.\n")

    @Rule(Fact(material='metal'))
    def R11(self):
        if self.yes_or_no("¿Es una herramienta? (si/no)? "):
            self.declare(Fact(herramienta=True))
        else:
            self.declare(Fact(adorno=True))

    @Rule(Fact(material='metal'), Fact(herramienta=True))
    def R12(self):
        if self.yes_or_no("¿Tiene un borde afilado? (si/no) "):
            self.declare(Fact(afilado=True))
        else:
            self.declare(Fact(afilado=False))

    @Rule(Fact(material='metal'), Fact(herramienta=True), Fact(afilado=True), Fact(detalles=False))
    def R13(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de metal, entonces es una herramienta de corte o arma  de uso recurrente como un cuchillo, un hacha o una punta de flecha.\n")

    @Rule(Fact(material='metal'), Fact(herramienta=True), Fact(afilado=True), Fact(detalles=True), Fact(ritual=True))
    def R14(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de metal y con alguna decoración, inscripcion o simbolo religioso, entonces es una herramienta de corte o arma como un cuchillo, un hacha o una punta de flecha, el cual se usa en rituales.\n")

    @Rule(Fact(material='metal'), Fact(herramienta=True), Fact(afilado=True), Fact(detalles=True), Fact(decorativo=True))
    def R15(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de metal y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una herramienta de corte o arma como un cuchillo, un hacha o una punta de flecha, el cual es un objeto decorativo o de prestigio.\n")

    @Rule(Fact(material='metal'), Fact(herramienta=True), Fact(afilado=False), Fact(detalles=False))
    def R16(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de metal, entonces es una herramienta de un uso general en algun oficio como la agricultura, cocina, raspar, etc.\n")

    @Rule(Fact(material='metal'), Fact(herramienta=True), Fact(afilado=False), Fact(detalles=True), Fact(ritual=True))
    def R17(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de metal y con alguna decoración, inscripcion o simbolo religioso, entonces es una herramienta de algun uso general, el cual se usa en rituales.\n")

    @Rule(Fact(material='metal'), Fact(herramienta=True), Fact(afilado=False), Fact(detalles=True), Fact(decorativo=True))
    def R18(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de metal y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una herramienta de un uso general algun oficio como la agricultura, cocina, raspar, etc., el cual es un objeto decorativo o de prestigio.\n")

    @Rule(Fact(adorno=True))
    def R19(self):
        if self.yes_or_no("¿Es una joya? (si/no) "):
            self.declare(Fact(joya=True))
        else:
            self.declare(Fact(figura=True))

    @Rule(Fact(joya=True))
    def R20(self):
        self.declare(Fact(detalles=True))

    @Rule(Fact(material='metal'), Fact(adorno=True), Fact(joya=True), Fact(detalles=True), Fact(ritual=True))
    def R21(self):
        print("El artefacto es un adorno con forma de joya, hecha a partir de metal y con alguna decoración, inscripcion o simbolo religioso, entonces es una joya que se usa en rituales.\n")

    @Rule(Fact(material='metal'), Fact(adorno=True), Fact(joya=True), Fact(detalles=True), Fact(decorativo=True))
    def R22(self):
        print("El artefacto es un adorno con forma de joya, hecha a partir de metal y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una joya, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(figura=True))
    def R23(self):
        if self.yes_or_no("¿Tiene la forma de algun Dios? (si/no) "):
            self.declare(Fact(deidad=True))
        elif self.yes_or_no("¿Tiene la forma humanoide? (si/no) "):
            self.declare(Fact(persona=True))
        else:
            self.declare(Fact(animal=True))

    @Rule(Fact(figura=True))
    def R24(self):
        self.declare(Fact(detalles=True))

    @Rule(Fact(material='metal'), Fact(adorno=True), Fact(figura=True), Fact(deidad=True), Fact(detalles=True), Fact(ritual=True))
    def R25(self):
        print("El artefacto es un adorno con forma de figura o escultura, en este caso siendo la representación de una deidad. Hecha a partir de metal y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de una deidad que se usa en rituales.\n")

    @Rule(Fact(material='metal'),  Fact(adorno=True), Fact(figura=True), Fact(deidad=True), Fact(detalles=True), Fact(decorativo=True))
    def R26(self):
        print("El artefacto es un adorno con forma de figura o escultura, , en este caso siendo la representación de una deidad. Hecha a partir de metal y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de una deidad, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='metal'), Fact(adorno=True), Fact(figura=True), Fact(persona=True), Fact(detalles=True), Fact(ritual=True))
    def R27(self):
        print("El artefacto es un adorno con forma de figura o escultura, en este caso siendo la representación de una persona. Hecha a partir de metal y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de una persona que se usa en rituales.\n")

    @Rule(Fact(material='metal'), Fact(adorno=True), Fact(figura=True), Fact(persona=True), Fact(detalles=True), Fact(decorativo=True))
    def R28(self):
        print("El artefacto es un adorno con forma de figura o escultura, , en este caso siendo la representación de una persona. Hecha a partir de metal y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de una persona, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='metal'), Fact(adorno=True), Fact(figura=True), Fact(animal=True), Fact(detalles=True), Fact(ritual=True))
    def R29(self):
        print("El artefacto es un adorno con forma de figura o escultura, en este caso siendo la representación de un animal. Hecha a partir de metal y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de un animal que se usa en rituales.\n")

    @Rule(Fact(material='metal'), Fact(adorno=True), Fact(figura=True), Fact(animal=True), Fact(detalles=True), Fact(decorativo=True))
    def R30(self):
        print("El artefacto es un adorno con forma de figura o escultura, , en este caso siendo la representación de una animal. Hecha a partir de metal y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de un animal, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='hueso'))
    def R31(self):
        if self.yes_or_no("¿Es una herramienta? (si/no) "):
            self.declare(Fact(herramienta=True))
        else:
            self.declare(Fact(adorno=True))

    @Rule(Fact(material='hueso'), Fact(herramienta=True))
    def R32(self):
        if self.yes_or_no("¿Tiene un borde afilado? (si/no) "):
            self.declare(Fact(afilado=True))
        elif self.yes_or_no("¿Es un punzón? (si/no) "):
            self.declare(Fact(punzon=True))
        else:
            self.declare(Fact(afilado=False))

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(afilado=True), Fact(detalles=False))
    def R33(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de hueso, entonces es una herramienta de corte o arma  de uso recurrente como un cuchillo o una punta de flecha.\n")

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(afilado=True), Fact(detalles=True), Fact(ritual=True))
    def R34(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de hueso y con alguna decoración, inscripcion o simbolo religioso, entonces es una herramienta de corte o arma como un cuchillo el cual se usa en rituales.\n")

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(afilado=True), Fact(detalles=True), Fact(decorativo=True))
    def R35(self):
        print("El artefacto es una herramienta lítica con un borde afilado, hecha a partir de hueso y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una herramienta de corte o arma como un cuchillo el cual es un objeto decorativo o de prestigio.\n")

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(afilado=False), Fact(detalles=False))
    def R36(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de hueso, entonces es una herramienta o utencilio en algun oficio como la agricultura, cocina, raspar, etc.\n")

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(afilado=False), Fact(detalles=True), Fact(ritual=True))
    def R37(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de hueso y con alguna decoración, inscripcion o simbolo religioso, entonces es una herramienta de algun uso general, el cual se usa en rituales.\n")

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(afilado=False), Fact(detalles=True), Fact(decorativo=True))
    def R38(self):
        print("El artefacto es una herramienta lítica plana y/o amplia, hecha a partir de hueso y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una herramienta o utencilio en algun oficio como la agricultura, cocina, raspar, etc., el cual es un objeto decorativo o de prestigio.\n")

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(punzon=True), Fact(detalles=True))
    def R39(self):
        print("El artefacto es una herramienta con forma de punzón, hecha a partir de hueso, entonces es una herramienta o utencilio para trabajar las pieles o el cuero.\n")

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(punzon=True), Fact(detalles=True), Fact(ritual=True))
    def R40(self):
        print("El artefacto es una herramienta con forma de punzón, hecha a partir de hueso y con alguna decoración, inscripcion o simbolo religioso, entonces es una herramienta punzante, el cual se usa en rituales.\n")

    @Rule(Fact(material='hueso'), Fact(herramienta=True), Fact(punzon=True), Fact(detalles=True), Fact(decorativo=True))
    def R41(self):
        print("El artefacto es una herramienta con forma de punzón, hecha a partir de hueso y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una herramienta o utencilio para trabajar las pieles o el cuero, el cual es un objeto decorativo o de prestigio.\n")

    @Rule(Fact(material='hueso'), Fact(adorno=True), Fact(joya=True), Fact(detalles=True), Fact(ritual=True))
    def R42(self):
        print("El artefacto es un adorno con forma de joya, hecha a partir de hueso y con alguna decoración, inscripcion o simbolo religioso, entonces es una joya que se usa en rituales.\n")

    @Rule(Fact(material='hueso'), Fact(adorno=True), Fact(joya=True), Fact(detalles=True), Fact(decorativo=True))
    def R43(self):
        print("El artefacto es un adorno con forma de joya, hecha a partir de hueso y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una joya, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='hueso'), Fact(adorno=True), Fact(figura=True), Fact(deidad=True), Fact(detalles=True), Fact(ritual=True))
    def R44(self):
        print("El artefacto es un adorno con forma de figura o escultura, en este caso siendo la representación de una deidad. Hecha a partir de hueso y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de una deidad que se usa en rituales.\n")

    @Rule(Fact(material='hueso'), Fact(adorno=True), Fact(figura=True), Fact(deidad=True), Fact(detalles=True), Fact(decorativo=True))
    def R45(self):
        print("El artefacto es un adorno con forma de figura o escultura, , en este caso siendo la representación de una deidad. Hecha a partir de hueso y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de una deidad, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='hueso'), Fact(adorno=True), Fact(figura=True), Fact(persona=True), Fact(detalles=True), Fact(ritual=True))
    def R46(self):
        print("El artefacto es un adorno con forma de figura o escultura, en este caso siendo la representación de una persona. Hecha a partir de hueso y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de una persona que se usa en rituales.\n")

    @Rule(Fact(material='hueso'), Fact(adorno=True), Fact(figura=True), Fact(persona=True), Fact(detalles=True), Fact(decorativo=True))
    def R47(self):
        print("El artefacto es un adorno con forma de figura o escultura, en este caso siendo la representación de una persona. Hecha a partir de hueso y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de una persona, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='hueso'), Fact(adorno=True), Fact(figura=True), Fact(animal=True), Fact(detalles=True), Fact(ritual=True))
    def R48(self):
        print("El artefacto es un adorno con forma de figura o escultura, en este caso siendo la representación de un animal. Hecha a partir de hueso y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de un animal que se usa en rituales.\n")

    @Rule(Fact(material='hueso'), Fact(adorno=True), Fact(figura=True), Fact(animal=True), Fact(detalles=True), Fact(decorativo=True))
    def R49(self):
        print("El artefacto es un adorno con forma de figura o escultura, en este caso siendo la representación de una animal. Hecha a partir de hueso y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de un animal, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='ceramica'))
    def R50(self):
        if self.yes_or_no("¿Es una vasija? (si/no) "):
            self.declare(Fact(vasija=True))
        else:
            self.declare(Fact(figura=True))

    @Rule(Fact(material='ceramica'), Fact(vasija=True))
    def R51(self):
        if self.yes_or_no("¿La vasija es profunda? (si/no) "):
            self.declare(Fact(profunda=True))
        else:
            self.declare(Fact(profunda=False))

    @Rule(Fact(material='ceramica'))
    def R52(self):
        if self.yes_or_no("¿La ceramica tiene pintura? (si/no) "):
            self.declare(Fact(pintura=True))
        else:
            self.declare(Fact(pintura=False))

    @Rule(Fact(material='ceramica'), Fact(pintura=True))
    def R53(self):
        if self.yes_or_no("¿La pintura es de colores brillantes? (si/no) "):
            self.declare(Fact(elaborada=True))
        else:
            self.declare(Fact(simple=True))

    @Rule(Fact(material='ceramica'), Fact(vasija=True), Fact(profunda=True), Fact(pintura=False))
    def R54(self):
        print("El artefacto es una vasija profunda por lo cual es una jarra o vaso, hecha a partir de ceramica de uso diario.\n")

    @Rule(Fact(material='ceramica'), Fact(vasija=True), Fact(profunda=True), Fact(pintura=True), Fact(simple=True))
    def R55(self):
        print("El artefacto es una vasija profunda por lo cual es una jarra o vaso, hecha a partir de ceramica con algo de pinturas simples siendo de uso diario.\n")

    @Rule(Fact(material='ceramica'), Fact(vasija=True), Fact(profunda=True), Fact(pintura=True), Fact(elaborada=True))
    def R56(self):
        print("El artefacto es una vasija profunda y tal vez con asas, por lo cual es una jarra o vaso, hecha a partir de ceramica con algo de pinturas de colores brillantes y elaborados siendo una ceramica de prestigio.\n")

    @Rule(Fact(material='ceramica'), Fact(vasija=True), Fact(profunda=False), Fact(pintura=False))
    def R57(self):
        print("El artefacto es una vasija poco profunda y tal vez abierta, por lo cual es una plato o recipiente poco profundo, hecha a partir de ceramica de uso diario.\n")

    @Rule(Fact(material='ceramica'), Fact(vasija=True), Fact(profunda=False), Fact(pintura=True), Fact(simple=True))
    def R58(self):
        print("El artefacto es una vasija poco profunda y tal vez abierta, por lo cual es una plato o recipiente poco profundo, hecha a partir de ceramica con algo de pinturas simples siendo de uso diario.\n")

    @Rule(Fact(material='ceramica'), Fact(vasija=True), Fact(profunda=True), Fact(pintura=True), Fact(elaborada=True))
    def R59(self):
        print("El artefacto es una vasija poco profunda y tal vez abierta, por lo cual es una plato o recipiente poco profundo, hecha a partir de ceramica con algo de pinturas de colores brillantes y elaborados siendo una ceramica de prestigio.\n")

    @Rule(Fact(material='ceramica'), Fact(figura=True), Fact(deidad=True), Fact(detalles=True), Fact(ritual=True))
    def R60(self):
        print("El artefacto es una figura o escultura, en este caso siendo la representación de una deidad. Hecha a partir de ceramica y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de una deidad que se usa en rituales.\n")

    @Rule(Fact(material='ceramica'), Fact(figura=True), Fact(deidad=True), Fact(detalles=True), Fact(decorativo=True))
    def R61(self):
        print("El artefacto es una figura o escultura, en este caso siendo la representación de una deidad. Hecha a partir de ceramica y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de una deidad, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='ceramica'), Fact(figura=True), Fact(persona=True), Fact(detalles=True), Fact(ritual=True))
    def R62(self):
        print("El artefacto es una figura o escultura, en este caso siendo la representación de una persona. Hecha a partir de ceramica y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de una persona que se usa en rituales.\n")

    @Rule(Fact(material='ceramica'), Fact(figura=True), Fact(persona=True), Fact(detalles=True), Fact(decorativo=True))
    def R63(self):
        print("El artefacto es una figura o escultura, en este caso siendo la representación de una persona. Hecha a partir de ceramica y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de una persona, ya sea decorativa o de prestigio.\n")

    @Rule(Fact(material='ceramica'), Fact(figura=True), Fact(animal=True), Fact(detalles=True), Fact(ritual=True))
    def R64(self):
        print("El artefacto es una figura o escultura, en este caso siendo la representación de un animal. Hecha a partir de ceramica y con alguna decoración, inscripcion o simbolo religioso, entonces es una escultura de un animal que se usa en rituales.\n")

    @Rule(Fact(material='ceramica'), Fact(figura=True), Fact(animal=True), Fact(detalles=True), Fact(decorativo=True))
    def R65(self):
        print("El artefacto es una figura o escultura, en este caso siendo la representación de una animal. Hecha a partir de ceramica y con alguna decoración, inscripcion o simbolo geométrico o asbtracto, entonces es una escultura de un animal, ya sea decorativa o de prestigio.\n")


if __name__ == "__main__":
    engine = SEArqueologia()
    engine.reset()
    engine.run()