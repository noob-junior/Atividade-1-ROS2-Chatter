Aooobaaaaa, tudo certo?
Serei o mais breve possivel, para n tomar muito do tempo de voces.

Minha atividade 1 é dividida basicamente em duas partes:
talker: um nó que publica uma string sem parar, em um loop de 1 egundo
listener: um nó que le e escreve no terminal o topico que o talker publicou

Para roda (abrir 2 terminais e escrever cada um deles, comandos especificos, em sequencia)

terminal 1:

cd ~/ros2_ws
source install/setup.bash
ros2 run my_chatter_pkg listener


terminal 2:

cd ~/ros2_ws
source install/setup.bash
ros2 run my_chatter_pkg talker




