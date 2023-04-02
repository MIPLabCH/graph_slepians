% Compute eigenvectors with smallest eigenvalues
% 
% returns
% Utr - truncated eigenbasis
% S1 - corresponding eigenvalues
%
% Dimitri Van De Ville, May 2017

function [Utr,S1]=slepEigsLaplacian(A,D,CONST_W,opts)

[Utr,S1]=eigs(@Binline,size(A,1),max(CONST_W),'sa',opts);

function y=Binline(x)
    y=D*x-A*x;
end

end
