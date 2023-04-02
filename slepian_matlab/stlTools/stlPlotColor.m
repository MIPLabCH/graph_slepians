function stlPlotColor(v, f, c, name)
%STLPLOT is an easy way to plot an STL object
%V is the Nx3 array of vertices
%F is the Mx3 array of faces
%C is the Vx1 array of grayscale values
%NAME is the name of the object, that will be displayed as a title

%figure;
object.vertices = v;
object.faces = f;
patch(object,'FaceColor',       'interp', ...
         'CDataMapping',     'scaled', ...
         'FaceVertexCData',  c, ...
         'EdgeColor',       'none',        ...
         'FaceLighting',    'gouraud',     ...
         'AmbientStrength', 0.15);

% Add a camera light, and tone down the specular highlighting
camlight('headlight');
material('dull');

colormap(jet);
caxis([-max(abs(c)) max(abs(c))]);

% Fix the axes scaling, and set a nice view angle
axis('image');
%view([-135 35]);
view([-15 3]);
grid on;
%title(name);
