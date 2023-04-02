% Demonstration script for Graph Slepians
% ---------------------------------------
%
% D. Van De Ville, R. Demesmaeker, M. G. Preti, 
% "When Slepian Meets Fiedler: Putting a Focus on the Graph Spectrum", 
% IEEE Signal Processing Letters, in press
%
%
% These scripts will reproduce the results of the above-mentioned paper. 
% Running the code on the CodeOcean platform takes typically between 1-4 minutes.
%
%
% http://miplab.epfl.ch/
%
% May 2017
% (c) Ecole Polytechnique Federale de Lausanne and University of Geneva


%% Setup environment
addpath('./stlTools/')

%% Settings
CONST_NUM_NODES=4567;
CONST_NORMALIZE=1;
CONST_OPERATOR=1;      % graph Laplacian
CONST_PRINT=1;

% Convention for index to store bases:
% 0: global (Laplacian eigenvectors)
% 1: Slepian with energy concentration
% 2: Slepian with graph embedding distance

%% Load data
[vertices,faces,normals,name] = stlRead('../data/oncapintada.stl');
i=[ faces(:,1); faces(:,1); faces(:,2); faces(:,2); faces(:,3); faces(:,3)];
j=[ faces(:,2); faces(:,3); faces(:,1); faces(:,3); faces(:,1); faces(:,2)];
A=sparse(i,j,ones(size(i,1),1),CONST_NUM_NODES,CONST_NUM_NODES);
NODES_XY=vertices;

%% Select head only (subgraph)
NODE_TYPE=ones(CONST_NUM_NODES,1)*2;
idx=find(NODES_XY(:,2)<-.4);
NODE_TYPE(idx)=1;
CONST_NODES{1}=idx;

if CONST_PRINT,
figure(1);
stlPlotColor(vertices,faces,NODE_TYPE-1,'');
grid off;
axis off;
view(-41,4)
saveas(gcf,'../results/fig-mesh-selection.png')
end;

%% Preprocess data, extract (truncated) graph spectrum
[A,D]=slepNormalize(A,CONST_NORMALIZE);

%% (1) Low-bandwidth example
CONST_W=9; % bandwidth
[basis,basis_eig0,basis_conc,basis_cut]=slepCompute(A,D,CONST_NODES,CONST_W,1);

figure(2);
for iter_GEN=1:3,
clf;
set(gcf,'Position',[590 528 530 400]);
for iter=1:9, 
    order=iter;
    row=2-floor((order-1)/3);
    col=mod(order-1,3);
    axes('Position',[1/3*col+.03 1/3*row 1/3 1/3]);
    name='';
    tmp=basis{iter_GEN}(:,iter);
    [~,idx]=max(abs(tmp));
    if sign(tmp(idx(1)))<0,
        tmp=-tmp;
    end;
    stlPlotColor(vertices,faces,tmp,name); 
    shading flat;
    axis off;
    axes('Position',[1/3*col 1/3*row 1/3 1/3]);
    axis off;
    text(0.02,.9,sprintf('%d',iter),'FontSize',14,'Interpreter','tex');
    PREFIX={'','',''};
    PREFIX{iter_GEN}='\bf';
    text(0.02,.8,sprintf('%s\\lambda=%4.3f',PREFIX{1},abs(basis_eig0{iter_GEN}(iter))),'FontSize',12,'Interpreter','tex');
    text(0.02,.7,sprintf('%s\\mu=%4.3f',PREFIX{2},abs(basis_conc{iter_GEN}(iter))),'FontSize',12,'Interpreter','tex');
    text(0.02,.6,sprintf('%s\\xi=%4.3f',PREFIX{3},abs(basis_cut{iter_GEN}(iter))),'FontSize',12,'Interpreter','tex');
end;

if CONST_PRINT==1,
    switch iter_GEN,
        case 1,
            fname='fig-mesh-lapl.png';
        case 2,
            fname='fig-mesh-slep-conc.png';
        case 3,
            fname='fig-mesh-slep-emb.png';
    end;
    saveas(gcf,sprintf('../results/%s',fname));
end;
end;

%% (2) High-bandwidth example 
CONST_W=1000; % bandwidth
[basis,basis_eig0,basis_conc,basis_cut]=slepCompute(A,D,CONST_NODES,CONST_W,0);

figure(3);

for iter_plot=1:3,
    clf;

    switch iter_plot,
        case 1,
            tmp=sort(reshape(cell2mat(basis_eig0),[CONST_W 3]));
            tmp_label='\lambda (embedded distance)'; fname='fig-plot-lapl.png';
            tmp_legend_location='NorthWest';
            tmp_x=1:CONST_W;
            tmp_xdir='normal';
        case 2,
            tmp=sort(reshape(cell2mat(basis_conc),[CONST_W 3]),'descend'); tmp_label='\mu (energy concentration)'; fname='fig-plot-slep-conc.png';
            tmp_legend_location='NorthWest';
            tmp_x=1:CONST_W;
            tmp_xdir='reverse';
        case 3,
            tmp=sort(reshape(cell2mat(basis_cut),[CONST_W 3])); tmp_label='\xi (modified embedded distance)'; fname='fig-plot-slep-emb.png';
            tmp_legend_location='NorthWest';
            tmp_x=1:CONST_W;
            tmp_xdir='normal';
    end;
    
    for iter=1:3,
        CONST_PLOT_OPTIONS={'k-','b-','r-'};
        h=plot(tmp_x,(tmp(:,iter)),CONST_PLOT_OPTIONS{iter});
        set(h,'LineWidth',2);
        set(gca, 'xdir',tmp_xdir)
        set(gca,'FontSize',14);
        hold on; 
    end;
    hold off;
    grid on;
    h=legend({'graph Laplacian','Slepian (energy concentration)','Slepian (modified distance)'},'Location',tmp_legend_location);
    set(h,'FontSize',16);
    xlabel('index','FontSize',16);
    ylabel(tmp_label,'FontSize',16);
    axis([1 CONST_W 0 max(tmp(:))]);
    
    if CONST_PRINT==1,
        saveas(gcf,sprintf('../results/%s',fname))
    end;
end;


%% Generate graph signal on mesh ('striped animal')
tmp0=sin(basis{1}(:,2)/max(abs(basis{1}(:,2)))*pi*8+pi);
CONST_FILTER=40;

figure(4);
for iter_plot=1:3,
    clf;
    
    switch iter_plot,
        case 1,
            tmpS=basis{1}.'*tmp0;
            tmp=basis{1}*tmpS;
            fname='fig-signal-orig.png';
        case 2,
            tmpS=basis{1}.'*tmp0;
            tmpS=tmpS.*exp(-basis_eig0{1}(:)*CONST_FILTER);
            tmp=basis{1}*tmpS;
            fname='fig-signal-filtered.png';
        case 3,
            tmpS=basis{3}.'*tmp0;
            tmpS=tmpS.*exp(-basis_cut{3}(:)*CONST_FILTER);
            tmp=basis{3}*tmpS;
            fname='fig-signal-slep-filtered.png';
    end;
    stlPlotColor(vertices,faces,tmp,'');
    caxis([-1 1]); grid off; axis off;
    view(-41,4);

    if CONST_PRINT==1,
        saveas(gcf,sprintf('../results/%s',fname));
    end;
end;

