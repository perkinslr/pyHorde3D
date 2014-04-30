# 1 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
# 1 "<command-line>"
# 1 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
# 15 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
       

# 1 "/home/perkins/svn/pyhorde/Horde3D.h" 1
# 15 "/home/perkins/svn/pyhorde/Horde3D.h"
       
# 27 "/home/perkins/svn/pyhorde/Horde3D.h"
# 1 "/usr/lib/gcc/x86_64-pc-linux-gnu/4.7.3/include/stdbool.h" 1 3 4
# 28 "/home/perkins/svn/pyhorde/Horde3D.h" 2
# 51 "/home/perkins/svn/pyhorde/Horde3D.h"
typedef int H3DRes;
typedef int H3DNode;





const H3DNode H3DRootNode = 1;



struct H3DOptions
{
# 88 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  MaxLogLevel = 1,
  MaxNumMessages,
  TrilinearFiltering,
  MaxAnisotropy,
  TexCompression,
  SRGBLinearization,
  LoadTextures,
  FastAnimation,
  ShadowMapSize,
  SampleCount,
  WireframeMode,
  DebugViewMode,
  DumpFailedShaders,
  GatherTimeStats
 };
};

struct H3DStats
{
# 126 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  TriCount = 100,
  BatchCount,
  LightPassCount,
  FrameTime,
  AnimationTime,
  GeoUpdateTime,
  ParticleSimTime,
  FwdLightsGPUTime,
  DefLightsGPUTime,
  ShadowsGPUTime,
  ParticleGPUTime,
  TextureVMem,
  GeometryVMem
 };
};

struct H3DResTypes
{
# 160 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  Undefined = 0,
  SceneGraph,
  Geometry,
  Animation,
  Material,
  Code,
  Shader,
  Texture,
  ParticleEffect,
  Pipeline
 };
};

struct H3DResFlags
{
# 189 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum Flags
 {
  NoQuery = 1,
  NoTexCompression = 2,
  NoTexMipmaps = 4,
  TexCubemap = 8,
  TexDynamic = 16,
  TexRenderable = 32,
  TexSRGB = 64
 };
};


struct H3DFormats
{
# 215 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  Unknown = 0,
  TEX_BGRA8,
  TEX_DXT1,
  TEX_DXT3,
  TEX_DXT5,
  TEX_RGBA16F,
  TEX_RGBA32F
 };
};


struct H3DGeoRes
{
# 243 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  GeometryElem = 200,
  GeoIndexCountI,
  GeoVertexCountI,
  GeoIndices16I,
  GeoIndexStream,
  GeoVertPosStream,
  GeoVertTanStream,
  GeoVertStaticStream
 };
};

struct H3DAnimRes
{






 enum List
 {
  EntityElem = 300,
  EntFrameCountI
 };
};

struct H3DMatRes
{
# 287 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  MaterialElem = 400,
  SamplerElem,
  UniformElem,
  MatClassStr,
  MatLinkI,
  MatShaderI,
  SampNameStr,
  SampTexResI,
  UnifNameStr,
  UnifValueF4
 };
};

struct H3DShaderRes
{
# 317 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  ContextElem = 600,
  SamplerElem,
  UniformElem,
  ContNameStr,
  SampNameStr,
  SampDefTexResI,
  UnifNameStr,
  UnifSizeI,
  UnifDefValueF4
 };
};

struct H3DTexRes
{
# 350 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  TextureElem = 700,
  ImageElem,
  TexFormatI,
  TexSliceCountI,
  ImgWidthI,
  ImgHeightI,
  ImgPixelStream
 };
};

struct H3DPartEffRes
{
# 381 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  ParticleElem = 800,
  ChanMoveVelElem,
  ChanRotVelElem,
  ChanSizeElem,
  ChanColRElem,
  ChanColGElem,
  ChanColBElem,
  ChanColAElem,
  PartLifeMinF,
  PartLifeMaxF,
  ChanStartMinF,
  ChanStartMaxF,
  ChanEndRateF,
  ChanDragElem
 };
};

struct H3DPipeRes
{







 enum List
 {
  StageElem = 900,
  StageNameStr,
  StageActivationI
 };
};


struct H3DNodeTypes
{
# 432 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  Undefined = 0,
  Group,
  Model,
  Mesh,
  Joint,
  Light,
  Camera,
  Emitter
 };
};

struct H3DNodeFlags
{
# 456 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  NoDraw = 1,
  NoCastShadow = 2,
  NoRayQuery = 4,
  Inactive = 7
 };
};

struct H3DNodeParams
{







 enum List
 {
  NameStr = 1,
  AttachmentStr
 };
};


struct H3DModel
{
# 498 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  GeoResI = 200,
  SWSkinningI,
  LodDist1F,
  LodDist2F,
  LodDist3F,
  LodDist4F
 };
};

struct H3DMesh
{
# 522 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  MatResI = 300,
  BatchStartI,
  BatchCountI,
  VertRStartI,
  VertREndI,
  LodLevelI
 };
};

struct H3DJoint
{





 enum List
 {
  JointIndexI = 400
 };
};

struct H3DLight
{
# 562 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  MatResI = 500,
  RadiusF,
  FovF,
  ColorF3,
  ColorMultiplierF,
  ShadowMapCountI,
  ShadowSplitLambdaF,
  ShadowMapBiasF,
  LightingContextStr,
  ShadowContextStr
 };
};

struct H3DCamera
{
# 598 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  PipeResI = 600,
  OutTexResI,
  OutBufIndexI,
  LeftPlaneF,
  RightPlaneF,
  BottomPlaneF,
  TopPlaneF,
  NearPlaneF,
  FarPlaneF,
  ViewportXI,
  ViewportYI,
  ViewportWidthI,
  ViewportHeightI,
  OrthoI,
  OccCullingI
 };
};

struct H3DEmitter
{
# 632 "/home/perkins/svn/pyhorde/Horde3D.h"
 enum List
 {
  MatResI = 700,
  PartEffResI,
  MaxCountI,
  RespawnCountI,
  DelayF,
  EmissionRateF,
  SpreadAngleF,
  ForceF3
 };
};


struct H3DModelUpdateFlags
{






 enum Flags
 {
  Animation = 1,
  Geometry = 2
 };
};
# 675 "/home/perkins/svn/pyhorde/Horde3D.h"
 const char *h3dGetVersionString();
# 689 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dCheckExtension( const char *extensionName );
# 710 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dGetError();
# 727 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dInit();
# 742 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dRelease();
# 759 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dRender( H3DNode cameraNode );
# 774 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dFinalizeFrame();
# 790 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dClear();
# 808 "/home/perkins/svn/pyhorde/Horde3D.h"
 const char *h3dGetMessage( int *level, float *time );
# 822 "/home/perkins/svn/pyhorde/Horde3D.h"
 float h3dGetOption( H3DOptions::List param );
# 837 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dSetOption( H3DOptions::List param, float value );
# 853 "/home/perkins/svn/pyhorde/Horde3D.h"
 float h3dGetStat( H3DStats::List param, _Bool reset );
# 881 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dShowOverlays( const float *verts, int vertCount, float colR, float colG, float colB,
                          float colA, H3DRes materialRes, int flags );
# 896 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dClearOverlays();
# 913 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dGetResType( H3DRes res );
# 931 "/home/perkins/svn/pyhorde/Horde3D.h"
 const char *h3dGetResName( H3DRes res );
# 950 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DRes h3dGetNextResource( int type, H3DRes start );
# 966 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DRes h3dFindResource( int type, const char *name );
# 984 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DRes h3dAddResource( int type, const char *name, int flags );
# 1002 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DRes h3dCloneResource( H3DRes sourceRes, const char *name );
# 1018 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dRemoveResource( H3DRes res );
# 1032 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dIsResLoaded( H3DRes res );
# 1052 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dLoadResource( H3DRes res, const char *data, int size );
# 1068 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dUnloadResource( H3DRes res );
# 1085 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dGetResElemCount( H3DRes res, int elem );
# 1105 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dFindResElem( H3DRes res, int elem, int param, const char *value );
# 1123 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dGetResParamI( H3DRes res, int elem, int elemIdx, int param );
# 1142 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetResParamI( H3DRes res, int elem, int elemIdx, int param, int value );
# 1162 "/home/perkins/svn/pyhorde/Horde3D.h"
 float h3dGetResParamF( H3DRes res, int elem, int elemIdx, int param, int compIdx );
# 1182 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetResParamF( H3DRes res, int elem, int elemIdx, int param, int compIdx, float value );
# 1203 "/home/perkins/svn/pyhorde/Horde3D.h"
 const char *h3dGetResParamStr( H3DRes res, int elem, int elemIdx, int param );
# 1222 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetResParamStr( H3DRes res, int elem, int elemIdx, int param, const char *value );
# 1247 "/home/perkins/svn/pyhorde/Horde3D.h"
 void *h3dMapResStream( H3DRes res, int elem, int elemIdx, int stream, _Bool read, _Bool write );
# 1261 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dUnmapResStream( H3DRes res );
# 1277 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DRes h3dQueryUnloadedResource( int index );
# 1293 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dReleaseUnusedResources();
# 1317 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DRes h3dCreateTexture( const char *name, int width, int height, int fmt, int flags );
# 1335 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetShaderPreambles( const char *vertPreamble, const char *fragPreamble );
# 1351 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dSetMaterialUniform( H3DRes materialRes, const char *name, float a, float b, float c, float d );
# 1370 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dResizePipelineBuffers( H3DRes pipeRes, int width, int height );
# 1398 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dGetRenderTargetData( H3DRes pipelineRes, const char *targetName, int bufIndex,
                                 int *width, int *height, int *compCount, void *dataBuffer, int bufferSize );
# 1416 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dGetNodeType( H3DNode node );
# 1431 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dGetNodeParent( H3DNode node );
# 1449 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dSetNodeParent( H3DNode node, H3DNode parent );
# 1465 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dGetNodeChild( H3DNode node, int index );
# 1484 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dAddNodes( H3DNode parent, H3DRes sceneGraphRes );
# 1498 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dRemoveNode( H3DNode node );
# 1517 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dCheckNodeTransFlag( H3DNode node, _Bool reset );
# 1536 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dGetNodeTransform( H3DNode node, float *tx, float *ty, float *tz,
                              float *rx, float *ry, float *rz, float *sx, float *sy, float *sz );
# 1555 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetNodeTransform( H3DNode node, float tx, float ty, float tz,
                              float rx, float ry, float rz, float sx, float sy, float sz );
# 1576 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dGetNodeTransMats( H3DNode node, const float **relMat, const float **absMat );
# 1592 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetNodeTransMat( H3DNode node, const float *mat4x4 );
# 1608 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dGetNodeParamI( H3DNode node, int param );
# 1625 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetNodeParamI( H3DNode node, int param, int value );
# 1643 "/home/perkins/svn/pyhorde/Horde3D.h"
 float h3dGetNodeParamF( H3DNode node, int param, int compIdx );
# 1661 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetNodeParamF( H3DNode node, int param, int compIdx, float value );
# 1680 "/home/perkins/svn/pyhorde/Horde3D.h"
 const char *h3dGetNodeParamStr( H3DNode node, int param );
# 1697 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetNodeParamStr( H3DNode node, int param, const char *value );
# 1711 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dGetNodeFlags( H3DNode node );
# 1727 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetNodeFlags( H3DNode node, int flags, _Bool recursive );
# 1745 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dGetNodeAABB( H3DNode node, float *minX, float *minY, float *minZ,
                         float *maxX, float *maxY, float *maxZ );
# 1764 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dFindNodes( H3DNode startNode, const char *name, int type );
# 1780 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dGetNodeFindResult( int index );
# 1798 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetNodeUniforms( H3DNode node, float *uniformData, int count );
# 1819 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dCastRay( H3DNode node, float ox, float oy, float oz, float dx, float dy, float dz, int numNearest );
# 1837 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dGetCastRayResult( int index, H3DNode *node, float *distance, float *intersection );
# 1859 "/home/perkins/svn/pyhorde/Horde3D.h"
 int h3dCheckNodeVisibility( H3DNode node, H3DNode cameraNode, _Bool checkOcclusion, _Bool calcLod );
# 1876 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dAddGroupNode( H3DNode parent, const char *name );
# 1894 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dAddModelNode( H3DNode parent, const char *name, H3DRes geometryRes );
# 1928 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetupModelAnimStage( H3DNode modelNode, int stage, H3DRes animationRes, int layer,
                                 const char *startNode, _Bool additive );
# 1954 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetModelAnimParams( H3DNode modelNode, int stage, float time, float weight );
# 1972 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dSetModelMorpher( H3DNode modelNode, const char *target, float weight );
# 1991 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dUpdateModel( H3DNode modelNode, int flags );
# 2013 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dAddMeshNode( H3DNode parent, const char *name, H3DRes materialRes,
                            int batchStart, int batchCount, int vertRStart, int vertREnd );
# 2032 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dAddJointNode( H3DNode parent, const char *name, int jointIndex );
# 2058 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dAddLightNode( H3DNode parent, const char *name, H3DRes materialRes,
                             const char *lightingContext, const char *shadowContext );
# 2077 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dAddCameraNode( H3DNode parent, const char *name, H3DRes pipelineRes );
# 2096 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dSetupCameraView( H3DNode cameraNode, float fov, float aspect, float nearDist, float farDist );
# 2112 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dGetCameraProjMat( H3DNode cameraNode, float *projMat );
# 2134 "/home/perkins/svn/pyhorde/Horde3D.h"
 H3DNode h3dAddEmitterNode( H3DNode parent, const char *name, H3DRes materialRes,
                               H3DRes particleEffectRes, int maxParticleCount, int respawnCount );
# 2152 "/home/perkins/svn/pyhorde/Horde3D.h"
 void h3dUpdateEmitter( H3DNode emitterNode, float timeDelta );
# 2169 "/home/perkins/svn/pyhorde/Horde3D.h"
 _Bool h3dHasEmitterFinished( H3DNode emitterNode );
# 18 "/home/perkins/svn/pyhorde/Horde3DUtils.h" 2
# 47 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
const int H3DUTMaxStatMode = 2;
# 63 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 void h3dutFreeMem( char **ptr );
# 78 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 _Bool h3dutDumpMessages();
# 96 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 _Bool h3dutInitOpenGL( int hDC );
# 112 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 void h3dutReleaseOpenGL();
# 129 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 void h3dutSwapBuffers();
# 149 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 const char *h3dutGetResourcePath( int type );
# 168 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 void h3dutSetResourcePath( int type, const char *path );
# 185 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 _Bool h3dutLoadResourcesFromDisk( const char *contentDir );
# 211 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 H3DRes h3dutCreateGeometryRes( const char *name, int numVertices, int numTriangleIndices,
           float *posData, unsigned int *indexData, short *normalData,
           short *tangentData, short *bitangentData,
           float *texData1, float *texData2 );
# 239 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 _Bool h3dutCreateTGAImage( const unsigned char *pixels, int width, int height, int bpp,
                              char **outData, int *outSize );
# 256 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 _Bool h3dutScreenshot( const char *filename );
# 278 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 void h3dutPickRay( H3DNode cameraNode, float nwx, float nwy, float *ox, float *oy, float *oz,
                       float *dx, float *dy, float *dz );
# 297 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 H3DNode h3dutPickNode( H3DNode cameraNode, float nwx, float nwy );
# 319 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 void h3dutShowText( const char *text, float x, float y, float size,
                        float colR, float colG, float colB, H3DRes fontMaterialRes );
# 338 "/home/perkins/svn/pyhorde/Horde3DUtils.h"
 void h3dutShowFrameStats( H3DRes fontMaterialRes, H3DRes panelMaterialRes, int mode );
