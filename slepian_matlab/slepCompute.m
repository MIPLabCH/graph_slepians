% Compute graph basis vectors 
% 
% returns
% basis - basis vectors (graph Laplacian, Slepian design 1, Slepian design 2017)
% basis_* - associated measures (Laplacian distance, concentration, modified distance)
%
% Dimitri Van De Ville, May 2017

function [basis,basis_eig0,basis_conc,basis_cut]=slepCompute(A,D,CONST_NODES,CONST_W,CONST_SCALED);

opts.issym=1;
opts.isreal=1;
opts.maxit=2500;
opts.disp=0;

idx=CONST_NODES{1};
idxW=1:CONST_W;

[Utr,S1]=slepEigsLaplacian(A,D,CONST_W,opts);
if CONST_SCALED,
    tmpS=sum(diag(S1(idxW,idxW)));
else    
    tmpS=1;
end;
S1=S1/tmpS;
tmpUS=Utr(idx,idxW)*sqrt(S1(idxW,idxW));
tmpU=Utr(idx,idxW);
C=tmpU.'*tmpU; C=real((C+C.')/2);
C2=tmpUS.'*tmpUS; C2=real((C2+C2.')/2);

%% Compute graph Slepians for all cases
for iter_GEN=0:2,

    if iter_GEN==0,
        SL0=Utr(:,idxW);
        eig0=diag(S1(idxW,idxW));
        conc=diag(C);
        cut=diag(C2);
    else
        lambda=iter_GEN-1; % 0 for regular Slepian, 1: for graph-embedding-distance Slepians
        Cmix=(1-lambda)*C+lambda*C2;
        
        [myV,myD]=eig(Cmix);
        SL0=Utr(:,idxW)*myV;
        eig0=diag(SL0.'*(D-A)*SL0); eig0=eig0(1:CONST_W)/tmpS;
        conc=diag(myV.'*C*myV);
        cut=diag(myV.'*C2*myV);
    end;
    basis{iter_GEN+1}=SL0;
    
    basis_eig0{iter_GEN+1}(:)=eig0;
    basis_conc{iter_GEN+1}(:)=conc;
    basis_cut{iter_GEN+1}(:)=cut;
end;
