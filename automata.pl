% Alejandro Adrián García Martínez A01707109
% Rutas del automata
route(a,0,a).
route(a,1,b).
route(a,2,f).
route(b,0,a).
route(b,1,c).
route(b,2,e).
route(c,0,a).
route(c,1,d).
route(c,2,f).
route(e,0,a).
route(e,1,g).
route(e,2,d).
route(f,0,a).
route(f,1,g).
route(f,2,f).
route(g,0,a).
route(g,1,h).
route(g,2,f).
route(d,0,a).
route(d,1,d).
route(d,2,f).
route(h,0,h).
route(h,1,h).
route(h,2,h).

% Este es el estado final al que se busca llegar si la secuencia es correcta
estado_final(d).

% Este es el inicio del automata donde recibe la lista y se coloca en la letra incial que es la a
inicio(Lista):-
    camino(Lista, a).

% Esta función nos sirve para revisar si ya se ha llegado al estado final así como verificar que no se vaya al caso trampa la letra h
camino([],Estado):-
    estado_final(Estado).

% En esta función se recorre la lista para verificar si es que es válida
camino([Set | Lista], Letra):-
    route(Letra,Set,X),
    camino(Lista,X).