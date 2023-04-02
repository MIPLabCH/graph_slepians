% Construct normalized (sparse) adjacency matrix
% 
% returns
% A - normalized adjacency matrix
% D - degree vector
%
% Dimitri Van De Ville, Sep 2014

function [A,D]=slepNormalize(A,CONST_NORMALIZE)

if ~issparse(A)
    warning('Adjacency matrix A is not sparse.');
end;

msize=size(A,1);

% normalize adjacency matrix
if CONST_NORMALIZE
    D=sum(A);
    Dn=D.^(-0.5);
    Dn=spdiags(Dn.',0,spalloc(msize,msize,msize));
    A=Dn*A*Dn;
    D=spdiags(ones(msize,1),0,spalloc(msize,msize,msize));
else
    D=spdiags(sum(A).',0,spalloc(msize,msize,msize));
end;

