
% AI Programming Example: Family Relations

% Facts
parent(john, mary).   % John is parent of Mary
parent(john, mike).
parent(susan, mary).
parent(susan, mike).

male(john).
male(mike).
female(susan).
female(mary).

% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.


% Queries: to be run in the Prolog terminal
% ?- father(john, mary).        % True
% ?- mother(susan, mike).       % True
% ?- grandparent(john, Child).  % Find John's grandchildren
% ?- sibling(mary, mike).       % True