import streamlit as st
import json
import random

# Define FFlag libraries for each performance mode
FFLAG_LIBRARIES = {
    "Max Performance": [
        {"FFlagGraphicsPerformanceBoost": "True"},
        {"DFFlagEnableAsyncTextureLoading": "True"},
        {"FFlagReduceRenderQuality": "True"},
        {"DFFlagOptimizeParticleSystems": "True"},
        {"FFlagDisableShadowCasting": "False"},
        {"DFFlagEnableFastPhysics": "True"},
        {"FFlagReduceTextureResolution": "True"},
        {"DFFlagEnableGPUAcceleration": "True"},
        {"FFlagMinimizePostEffects": "True"},
        {"FFlagOptimizeMeshLoading": "True"},
        {"FFlagEnableParallelRendering": "True"},
        {"FFlagReduceAnimationFrames": "True"},
        {"FFlagDisableTerrainDetails": "True"},
        {"DFFlagEnableLODSystem": "True"},
        {"FFlagOptimizeNetworkReplication": "True"},
        {"FFlagReduceShaderComplexity": "True"},
        {"FFlagEnableDynamicResolution": "True"},
        {"FFlagDisableVolumetricFog": "True"},
        {"FFlagOptimizeSoundProcessing": "True"},
        {"FFlagEnableFrameBufferOptimization": "True"},
        {"FFlagReduceParticleDensity": "True"},
        {"FFlagEnableAsyncAssetLoading": "True"},
        {"FFlagDisableReflectionProbes": "True"},
        {"FFlagOptimizeLightingSystem": "True"},
        {"FFlagEnableMinimalUI": "True"},
        {"FFlagReduceBloomIntensity": "True"},
        {"FFlagDisableDepthOfField": "True"},
        {"FFlagOptimizeScriptExecution": "True"},
        {"FFlagEnableCullDistance": "True"},
        {"FFlagReduceTextureAnisotropy": "True"},
        {"FFlagDisableDynamicShadows": "True"},
        {"FFlagEnableFastStartup": "True"},
        {"FFlagOptimizeMemoryUsage": "True"},
        {"FFlagReducePhysicsCalculations": "True"},
        {"FFlagEnableStreamedTextures": "True"},
        {"FFlagDisableAmbientOcclusion": "True"},
        {"FFlagOptimizePathfinding": "True"},
        {"FFlagEnableLowResBuffers": "True"},
        {"FFlagReduceNetworkPackets": "True"},
        {"FFlagEnableTextureCompression": "True"},
        {"FFlagDisableLensFlares": "True"},
        {"FFlagOptimizeCollisionDetection": "True"},
        {"FFlagEnableMinimalPostProcessing": "True"},
        {"FFlagReduceSoundChannels": "True"},
        {"FFlagEnableEfficientCulling": "True"},
        {"FFlagOptimizeRenderPipeline": "True"},
        {"FFlagDisableSkybox": "True"},
        {"FFlagEnableFastMaterialLoading": "True"},
        {"FFlagReduceVertexBuffers": "True"},
    ],
    "Low-End Device": [
        {"FFlagGraphicsPerformanceBoost": "True"},
        {"DFFlagEnableAsyncTextureLoading": "True"},
        {"FFlagReduceRenderQuality": "True"},
        {"FFlagDisableShadowCasting": "True"},
        {"DFFlagEnableMinimalGraphics": "True"},
        {"FFlagDisablePostEffects": "True"},
        {"FFlagReduceTextureResolution": "True"},
        {"FFlagDisableVolumetricFog": "True"},
        {"DFFlagEnableLowDetailLOD": "True"},
        {"FFlagDisableTerrainDetails": "True"},
        {"FFlagReduceParticleEffects": "True"},
        {"FFlagEnableSimpleShaders": "True"},
        {"FFlagDisableDynamicLighting": "True"},
        {"FFlagReduceAnimationFrames": "True"},
        {"FFlagEnableTextureCompression": "True"},
        {"FFlagDisableReflectionProbes": "True"},
        {"FFlagOptimizeMemoryUsage": "True"},
        {"FFlagReducePhysicsCalculations": "True"},
        {"FFlagEnableLowResBuffers": "True"},
        {"FFlagDisableAmbientOcclusion": "True"},
        {"FFlagReduceSoundChannels": "True"},
        {"FFlagEnableMinimalUI": "True"},
        {"FFlagDisableBloom": "True"},
        {"FFlagOptimizeCollisionDetection": "True"},
        {"FFlagEnableFastStartup": "True"},
        {"FFlagReduceShaderComplexity": "True"},
        {"FFlagDisableLensFlares": "True"},
        {"FFlagEnableStreamedTextures": "True"},
        {"FFlagOptimizePathfinding": "True"},
        {"FFlagDisableSkybox": "True"},
        {"FFlagReduceVertexBuffers": "True"},
        {"FFlagEnableEfficientCulling": "True"},
        {"FFlagDisableDepthOfField": "True"},
        {"FFlagOptimizeScriptExecution": "True"},
        {"FFlagReduceNetworkPackets": "True"},
        {"FFlagEnableDynamicResolution": "True"},
        {"FFlagDisableDynamicShadows": "True"},
        {"FFlagOptimizeRenderPipeline": "True"},
        {"FFlagEnableFastMaterialLoading": "True"},
        {"FFlagReduceBloomIntensity": "True"},
        {"FFlagEnableMinimalPostProcessing": "True"},
        {"FFlagOptimizeLightingSystem": "True"},
        {"FFlagReduceTextureAnisotropy": "True"},
        {"FFlagEnableCullDistance": "True"},
        {"FFlagOptimizeSoundProcessing": "True"},
        {"FFlagEnableFrameBufferOptimization": "True"},
        {"FFlagReduceParticleDensity": "True"},
        {"FFlagEnableAsyncAssetLoading": "True"},
    ],
    "High FPS": [
        {"FFlagGraphicsPerformanceBoost": "True"},
        {"DFFlagEnableAsyncTextureLoading": "True"},
        {"FFlagOptimizeParticleSystems": "True"},
        {"FFlagReduceRenderQuality": "True"},
        {"DFFlagEnableFastPhysics": "True"},
        {"FFlagEnableParallelRendering": "True"},
        {"FFlagReduceAnimationFrames": "True"},
        {"DFFlagEnableLODSystem": "True"},
        {"FFlagOptimizeNetworkReplication": "True"},
        {"FFlagReduceShaderComplexity": "True"},
        {"FFlagEnableDynamicResolution": "True"},
        {"FFlagOptimizeSoundProcessing": "True"},
        {"FFlagEnableFrameBufferOptimization": "True"},
        {"FFlagReduceParticleDensity": "True"},
        {"FFlagEnableAsyncAssetLoading": "True"},
        {"FFlagOptimizeLightingSystem": "True"},
        {"FFlagEnableMinimalUI": "True"},
        {"FFlagReduceBloomIntensity": "True"},
        {"FFlagOptimizeScriptExecution": "True"},
        {"FFlagEnableCullDistance": "True"},
        {"FFlagReduceTextureAnisotropy": "True"},
        {"FFlagEnableFastStartup": "True"},
        {"FFlagOptimizeMemoryUsage": "True"},
        {"FFlagReducePhysicsCalculations": "True"},
        {"FFlagEnableStreamedTextures": "True"},
        {"FFlagOptimizePathfinding": "True"},
        {"FFlagEnableLowResBuffers": "True"},
        {"FFlagReduceNetworkPackets": "True"},
        {"FFlagEnableTextureCompression": "True"},
        {"FFlagOptimizeCollisionDetection": "True"},
        {"FFlagEnableMinimalPostProcessing": "True"},
        {"FFlagReduceSoundChannels": "True"},
        {"FFlagEnableEfficientCulling": "True"},
        {"FFlagOptimizeRenderPipeline": "True"},
        {"FFlagEnableFastMaterialLoading": "True"},
        {"FFlagReduceVertexBuffers": "True"},
        {"FFlagDisableSkybox": "True"},
        {"FFlagDisableVolumetricFog": "True"},
        {"FFlagDisableReflectionProbes": "True"},
        {"FFlagDisableAmbientOcclusion": "True"},
        {"FFlagDisableDynamicShadows": "True"},
        {"FFlagDisableDepthOfField": "True"},
        {"FFlagDisableLensFlares": "True"},
        {"FFlagDisableBloom": "True"},
        {"FFlagEnableGPUAcceleration": "True"},
        {"FFlagMinimizePostEffects": "True"},
        {"FFlagOptimizeMeshLoading": "True"},
    ],
    "Low Ping": [
        {"FFlagOptimizeNetworkReplication": "True"},
        {"DFFlagReduceNetworkPackets": "True"},
        {"FFlagEnableEfficientCulling": "True"},
        {"FFlagOptimizeScriptExecution": "True"},
        {"FFlagReducePhysicsCalculations": "True"},
        {"FFlagEnableFastStartup": "True"},
        {"FFlagOptimizePathfinding": "True"},
        {"FFlagEnableAsyncAssetLoading": "True"},
        {"FFlagReduceParticleDensity": "True"},
        {"FFlagEnableStreamedTextures": "True"},
        {"FFlagOptimizeCollisionDetection": "True"},
        {"FFlagReduceSoundChannels": "True"},
        {"FFlagEnableMinimalUI": "True"},
        {"FFlagOptimizeMemoryUsage": "True"},
        {"FFlagEnableTextureCompression": "True"},
        {"FFlagReduceVertexBuffers": "True"},
        {"FFlagEnableLowResBuffers": "True"},
        {"FFlagOptimizeRenderPipeline": "True"},
        {"FFlagEnableFastMaterialLoading": "True"},
        {"FFlagReduceAnimationFrames": "True"},
        {"FFlagEnableCullDistance": "True"},
        {"FFlagReduceTextureAnisotropy": "True"},
        {"FFlagEnableDynamicResolution": "True"},
        {"FFlagOptimizeSoundProcessing": "True"},
        {"FFlagEnableFrameBufferOptimization": "True"},
        {"FFlagGraphicsPerformanceBoost": "True"},
        {"DFFlagEnableAsyncTextureLoading": "True"},
        {"FFlagReduceShaderComplexity": "True"},
        {"DFFlagEnableLODSystem": "True"},
        {"FFlagOptimizeLightingSystem": "True"},
        {"FFlagReduceBloomIntensity": "True"},
        {"FFlagDisableVolumetricFog": "True"},
        {"FFlagDisableReflectionProbes": "True"},
        {"FFlagDisableAmbientOcclusion": "True"},
        {"FFlagDisableDynamicShadows": "True"},
        {"FFlagDisableDepthOfField": "True"},
        {"FFlagDisableLensFlares": "True"},
        {"FFlagDisableBloom": "True"},
        {"FFlagEnableGPUAcceleration": "True"},
        {"FFlagMinimizePostEffects": "True"},
        {"FFlagOptimizeMeshLoading": "True"},
        {"FFlagEnableParallelRendering": "True"},
        {"FFlagReduceRenderQuality": "True"},
        {"DFFlagEnableFastPhysics": "True"},
        {"FFlagReduceTextureResolution": "True"},
        {"FFlagDisableTerrainDetails": "True"},
        {"FFlagDisableSkybox": "True"},
    ],
    "Texture Optimization": [
        {"FFlagReduceTextureResolution": "True"},
        {"DFFlagEnableAsyncTextureLoading": "True"},
        {"FFlagEnableTextureCompression": "True"},
        {"FFlagEnableStreamedTextures": "True"},
        {"FFlagReduceTextureAnisotropy": "True"},
        {"FFlagOptimizeMeshLoading": "True"},
        {"FFlagEnableFastMaterialLoading": "True"},
        {"FFlagReduceVertexBuffers": "True"},
        {"FFlagEnableLowResBuffers": "True"},
        {"FFlagGraphicsPerformanceBoost": "True"},
        {"FFlagReduceRenderQuality": "True"},
        {"DFFlagEnableLODSystem": "True"},
        {"FFlagOptimizeNetworkReplication": "True"},
        {"FFlagReduceShaderComplexity": "True"},
        {"FFlagEnableDynamicResolution": "True"},
        {"FFlagDisableVolumetricFog": "True"},
        {"FFlagOptimizeSoundProcessing": "True"},
        {"FFlagEnableFrameBufferOptimization": "True"},
        {"FFlagReduceParticleDensity": "True"},
        {"FFlagEnableAsyncAssetLoading": "True"},
        {"FFlagDisableReflectionProbes": "True"},
        {"FFlagOptimizeLightingSystem": "True"},
        {"FFlagEnableMinimalUI": "True"},
        {"FFlagReduceBloomIntensity": "True"},
        {"FFlagDisableDepthOfField": "True"},
        {"FFlagOptimizeScriptExecution": "True"},
        {"FFlagEnableCullDistance": "True"},
        {"FFlagDisableDynamicShadows": "True"},
        {"FFlagEnableFastStartup": "True"},
        {"FFlagOptimizeMemoryUsage": "True"},
        {"FFlagReducePhysicsCalculations": "True"},
        {"FFlagDisableAmbientOcclusion": "True"},
        {"FFlagOptimizePathfinding": "True"},
        {"FFlagReduceNetworkPackets": "True"},
        {"FFlagDisableLensFlares": "True"},
        {"FFlagOptimizeCollisionDetection": "True"},
        {"FFlagEnableMinimalPostProcessing": "True"},
        {"FFlagReduceSoundChannels": "True"},
        {"FFlagEnableEfficientCulling": "True"},
        {"FFlagOptimizeRenderPipeline": "True"},
        {"FFlagDisableSkybox": "True"},
        {"FFlagEnableGPUAcceleration": "True"},
        {"FFlagMinimizePostEffects": "True"},
        {"FFlagEnableParallelRendering": "True"},
        {"FFlagReduceAnimationFrames": "True"},
        {"FFlagDisableTerrainDetails": "True"},
        {"FFlagOptimizeParticleSystems": "True"},
        {"DFFlagEnableFastPhysics": "True"},
    ],
    "Balanced Mode": [
        {"FFlagGraphicsPerformanceBoost": "True"},
        {"DFFlagEnableAsyncTextureLoading": "True"},
        {"FFlagReduceRenderQuality": "True"},
        {"FFlagOptimizeParticleSystems": "True"},
        {"DFFlagEnableFastPhysics": "True"},
        {"FFlagReduceTextureResolution": "True"},
        {"FFlagEnableGPUAcceleration": "True"},
        {"FFlagMinimizePostEffects": "True"},
        {"FFlagOptimizeMeshLoading": "True"},
        {"FFlagEnableParallelRendering": "True"},
        {"FFlagReduceAnimationFrames": "True"},
        {"DFFlagEnableLODSystem": "True"},
        {"FFlagOptimizeNetworkReplication": "True"},
        {"FFlagReduceShaderComplexity": "True"},
        {"FFlagEnableDynamicResolution": "True"},
        {"FFlagDisableVolumetricFog": "True"},
        {"FFlagOptimizeSoundProcessing": "True"},
        {"FFlagEnableFrameBufferOptimization": "True"},
        {"FFlagReduceParticleDensity": "True"},
        {"FFlagEnableAsyncAssetLoading": "True"},
        {"FFlagDisableReflectionProbes": "True"},
        {"FFlagOptimizeLightingSystem": "True"},
        {"FFlagEnableMinimalUI": "True"},
        {"FFlagReduceBloomIntensity": "True"},
        {"FFlagDisableDepthOfField": "True"},
        {"FFlagOptimizeScriptExecution": "True"},
        {"FFlagEnableCullDistance": "True"},
        {"FFlagReduceTextureAnisotropy": "True"},
        {"FFlagDisableDynamicShadows": "True"},
        {"FFlagEnableFastStartup": "True"},
        {"FFlagOptimizeMemoryUsage": "True"},
        {"FFlagReducePhysicsCalculations": "True"},
        {"FFlagEnableStreamedTextures": "True"},
        {"FFlagDisableAmbientOcclusion": "True"},
        {"FFlagOptimizePathfinding": "True"},
        {"FFlagEnableLowResBuffers": "True"},
        {"FFlagReduceNetworkPackets": "True"},
        {"FFlagEnableTextureCompression": "True"},
        {"FFlagDisableLensFlares": "True"},
        {"FFlagOptimizeCollisionDetection": "True"},
        {"FFlagEnableMinimalPostProcessing": "True"},
        {"FFlagReduceSoundChannels": "True"},
        {"FFlagEnableEfficientCulling": "True"},
        {"FFlagOptimizeRenderPipeline": "True"},
        {"FFlagDisableSkybox": "True"},
        {"FFlagEnableFastMaterialLoading": "True"},
        {"FFlagReduceVertexBuffers": "True"},
    ],
    "Ultra-Low Latency": [
        {"FFlagOptimizeNetworkReplication": "True"},
        {"DFFlagReduceNetworkPackets": "True"},
        {"FFlagEnableEfficientCulling": "True"},
        {"FFlagOptimizeScriptExecution": "True"},
        {"FFlagReducePhysicsCalculations": "True"},
        {"FFlagEnableFastStartup": "True"},
        {"FFlagOptimizePathfinding": "True"},
        {"FFlagEnableAsyncAssetLoading": "True"},
        {"FFlagReduceParticleDensity": "True"},
        {"FFlagEnableStreamedTextures": "True"},
        {"FFlagOptimizeCollisionDetection": "True"},
        {"FFlagReduceSoundChannels": "True"},
        {"FFlagEnableMinimalUI": "True"},
        {"FFlagOptimizeMemoryUsage": "True"},
        {"FFlagEnableTextureCompression": "True"},
        {"FFlagReduceVertexBuffers": "True"},
        {"FFlagEnableLowResBuffers": "True"},
        {"FFlagOptimizeRenderPipeline": "True"},
        {"FFlagEnableFastMaterialLoading": "True"},
        {"FFlagReduceAnimationFrames": "True"},
        {"FFlagEnableCullDistance": "True"},
        {"FFlagReduceTextureAnisotropy": "True"},
        {"FFlagEnableDynamicResolution": "True"},
        {"FFlagOptimizeSoundProcessing": "True"},
        {"FFlagEnableFrameBufferOptimization": "True"},
        {"FFlagGraphicsPerformanceBoost": "True"},
        {"DFFlagEnableAsyncTextureLoading": "True"},
        {"FFlagReduceShaderComplexity": "True"},
        {"DFFlagEnableLODSystem": "True"},
        {"FFlagOptimizeLightingSystem": "True"},
        {"FFlagReduceBloomIntensity": "True"},
        {"FFlagDisableVolumetricFog": "True"},
        {"FFlagDisableReflectionProbes": "True"},
        {"FFlagDisableAmbientOcclusion": "True"},
        {"FFlagDisableDynamicShadows": "True"},
        {"FFlagDisableDepthOfField": "True"},
        {"FFlagDisableLensFlares": "True"},
        {"FFlagDisableBloom": "True"},
        {"FFlagEnableGPUAcceleration": "True"},
        {"FFlagMinimizePostEffects": "True"},
        {"FFlagOptimizeMeshLoading": "True"},
        {"FFlagEnableParallelRendering": "True"},
        {"FFlagReduceRenderQuality": "True"},
        {"DFFlagEnableFastPhysics": "True"},
        {"FFlagReduceTextureResolution": "True"},
        {"FFlagDisableTerrainDetails": "True"},
        {"FFlagDisableSkybox": "True"},
    ],
}

# Streamlit app configuration
st.set_page_config(page_title="Roblox FFlag Generator", layout="centered")

# Custom CSS for mobile-friendliness and clean design
st.markdown("""
    <style>
    body {
        font-family: Arial, sans-serif;
    }
    .stApp {
        max-width: 800px;
        margin: 0 auto;
        padding: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #135e96;
    }
    .stSelectbox {
        width: 100%;
    }
    .stMarkdown {
        text-align: center;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #555;
    }
    pre {
        background-color: #f6f8fa;
        padding: 10px;
        border-radius: 5px;
        overflow-x: auto;
        font-size: 14px;
    }
    @media (max-width: 600px) {
        .stApp {
            padding: 5px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 8px;
        }
        pre {
            font-size: 12px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for mode selection
st.sidebar.title("Performance Modes")
mode = st.sidebar.selectbox(
    "Select Mode",
    [
        "Max Performance",
        "Low-End Device",
        "High FPS",
        "Low Ping",
        "Texture Optimization",
        "Balanced Mode",
        "Ultra-Low Latency",
    ],
    index=0,
)

# Main content
st.title("Roblox FFlag Generator")
st.markdown("Select a performance mode and generate optimized FFlags for Roblox.")

# Generate FFlags button
if st.button("Generate FFlags"):
    # Randomly select 10–15 FFlags from the selected mode's library
    selected_fflags = random.sample(FFLAG_LIBRARIES[mode], random.randint(10, 15))
    
    # Combine into a single dictionary
    combined_fflags = {}
    for fflag in selected_fflags:
        combined_fflags.update(fflag)
    
    # Convert to formatted JSON
    formatted_json = json.dumps(combined_fflags, indent=2)
    
    # Store in session state for downloading
    st.session_state["generated_fflags"] = formatted_json
    
    # Display formatted JSON
    st.markdown("### Generated FFlags")
    st.code(formatted_json, language="json")
    
    # Download button for JSON
    st.download_button(
        label="Download FFlags",
        data=formatted_json,
        file_name="fflags.json",
        mime="application/json"
    )

# Display previously generated FFlags if they exist
elif "generated_fflags" in st.session_state:
    st.markdown("### Generated FFlags")
    st.code(st.session_state["generated_fflags"], language="json")
    
    # Download button for JSON
    st.download_button(
        label="Download FFlags",
        data=st.session_state["generated_fflags"],
        file_name="fflags.json",
        mime="application/json"
    )

# Footer
st.markdown('<div class="footer">Made by KELSIER 🗡️(kelsier_69 on discord)</div>', unsafe_allow_html=True)
