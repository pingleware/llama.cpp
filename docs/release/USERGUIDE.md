# LLAMA.CPP User Guide
When compiled, produces the following executables

Here’s a breakdown of the potential applications or purposes of the listed executables related to LLaMA models:

1. **llama-baby-llama.exe**: Likely a variant or lightweight version of the LLaMA model or framework, potentially optimized for smaller systems or specific tasks.

2. **llama-batched.exe**: Executes batched inference or operations, where multiple inputs are processed in parallel to improve efficiency.

3. **llama-batched-bench.exe**: A benchmarking tool for testing batched inference performance, measuring the speed and throughput.

4. **llama-bench.exe**: A general benchmarking tool for testing the performance of LLaMA model inference or operations.

5. **llama-bench-matmult.exe**: A specialized benchmarking tool focusing on matrix multiplication performance, which is crucial for deep learning model inference.

6. **llama-cli.exe**: A command-line interface for interacting with LLaMA models, enabling tasks like inference or model management via CLI commands.

7. **llama-convert-llama2c-to-ggml.exe**: Converts models from the LLaMA 2C format to GGML (General Graphical Model Language), possibly for better compatibility or performance optimization.

8. **llama-cvector-generator.exe**: Generates contextual or embedding vectors for input text using the LLaMA model, useful for tasks like similarity search or embeddings.

9. **llama-embedding.exe**: Creates embeddings from text, which can be used in various applications such as retrieval-augmented generation or text classification.

10. **llama-eval-callback.exe**: Likely evaluates a model or inference task with callback functionality, providing custom feedback during or after evaluation.

11. **llama-export-lora.exe**: Exports a model using the LoRA (Low-Rank Adaptation) technique, typically used to fine-tune models efficiently.

12. **llama-gbnf-validator.exe**: Validates grammar-based neural frameworks (GBNF), which may involve checking syntax or consistency in input text processing.

13. **llama-gguf.exe**: Converts or processes models in the GGUF (General Graphical Universal Format), a format related to model deployment.

14. **llama-gguf-hash.exe**: Computes hashes or checksums for GGUF files, ensuring the integrity of model data or format compatibility.

15. **llama-gguf-split.exe**: Splits GGUF model files into smaller parts, possibly for easier handling, distribution, or loading in memory-constrained environments.

16. **llama-gritlm.exe**: Refers to GRIT (Graph Representation of Information Transfer) LM, possibly a specific variant or task related to LLaMA for transfer learning.

17. **llama-imatrix.exe**: Likely deals with matrix operations or transformations, integral to neural network computations.

18. **llama-infill.exe**: Likely used for infilling text, where the model predicts and fills in missing parts of a given text sequence.

19. **llama-llava-cli.exe**: A CLI for LLAVA (Large Language and Vision Assistant), integrating LLaMA with vision tasks or multimodal applications.

20. **llama-lookahead.exe**: Implements lookahead techniques, potentially for improving optimization or inference speed by precomputing next steps.

21. **llama-lookup.exe**: Likely performs lookups, possibly in an embeddings space or a retrieval database.

22. **llama-lookup-create.exe**: Creates lookup tables or indices, useful in retrieval-augmented generation or search applications.

23. **llama-lookup-merge.exe**: Merges lookup tables or indices, possibly to combine different datasets or model outputs.

24. **llama-lookup-stats.exe**: Provides statistics on lookup tables, like performance, hit rates, or memory usage.

25. **llama-minicpmv-cli.exe**: A CLI interface for MiniCPMV (likely a compressed version of the model), enabling compact inference or task execution.

26. **llama-parallel.exe**: Executes model inference or operations in parallel, optimizing performance by distributing tasks across CPU cores.

27. **llama-passkey.exe**: Possibly deals with authentication or encryption tasks within the LLaMA framework, using passkeys for access control.

28. **llama-perplexity.exe**: Measures perplexity, a common metric for evaluating the performance of language models.

29. **llama-q8dot.exe**: Likely involves 8-bit quantization with dot product operations, which optimizes the model for faster inference with lower precision.

30. **llama-quantize.exe**: Quantizes a model, reducing its size and improving inference speed by lowering the precision of weights and activations.

31. **llama-quantize-stats.exe**: Provides statistics and analysis on the quantization process, like model size reduction and performance impact.

32. **llama-retrieval.exe**: Handles retrieval operations, fetching relevant documents or embeddings based on input queries.

33. **llama-save-load-state.exe**: Saves and loads model states, useful for checkpointing or resuming long-running tasks.

34. **llama-server.exe**: Runs the LLaMA model as a server, allowing API-based interactions for inference or embedding generation.

35. **llama-simple.exe**: A simplified version of the LLaMA model, possibly with a smaller architecture or fewer features.

36. **llama-speculative.exe**: Performs speculative decoding or execution, where future steps are predicted and precomputed to improve efficiency.

37. **llama-tokenize.exe**: Tokenizes input text, preparing it for model inference by converting text into tokens.

38. **llama-vdot.exe**: Likely involves vector dot product operations, integral to neural network computations for tasks like attention mechanisms or similarity searches.

## llama-baby-llama.exe

## llama-batched.exe

## llama-batched-bench.exe

## llama-bench.exe

## llama-bench-matmult.exe

## llama-cli.exe

## llama-convert-llama2c-to-ggml.exe

## llama-cvector-generator.exe

## llama-embedding.exe

## llama-eval-callback.exe

## llama-export-lora.exe

## llama-gbnf-validator.exe

## llama-gguf.exe

## llama-gguf-hash.exe

## llama-gguf-split.exe

## llama-gritlm.exe

## llama-imatrix.exe

## llama-infill.exe

## llama-llava-cli.exe

## llama-lookahead.exe

## llama-lookup.exe

## llama-lookup-create.exe

## llama-lookup-merge.exe

## llama-lookup-stats.exe

## llama-minicpmv-cli.exe

## llama-parallel.exe

## llama-passkey.exe

## llama-perplexity.exe

## llama-q8dot.exe

## llama-quantize.exe

## llama-quantize-stats.exe

## llama-retrieval.exe

----- common params -----
```
-h,    --help, --usage                  print usage and exit
--version                               show version and build info
-v,    --verbose                        print verbose information
--verbosity N                           set specific verbosity level (default: 0)
-t,    --threads N                      number of threads to use during generation (default: -1)
                                        (env: LLAMA_ARG_THREADS)
-tb,   --threads-batch N                number of threads to use during batch and prompt processing (default:
                                        same as --threads)
-C,    --cpu-mask M                     CPU affinity mask: arbitrarily long hex. Complements cpu-range
                                        (default: "")
-Cr,   --cpu-range lo-hi                range of CPUs for affinity. Complements --cpu-mask
--cpu-strict <0|1>                      use strict CPU placement (default: 0)
--prio N                                set process/thread priority : 0-normal, 1-medium, 2-high, 3-realtime
                                        (default: 0)
--poll <0...100>                        use polling level to wait for work (0 - no polling, default: 50)
-Cb,   --cpu-mask-batch M               CPU affinity mask: arbitrarily long hex. Complements cpu-range-batch
                                        (default: same as --cpu-mask)
-Crb,  --cpu-range-batch lo-hi          ranges of CPUs for affinity. Complements --cpu-mask-batch
--cpu-strict-batch <0|1>                use strict CPU placement (default: same as --cpu-strict)
--prio-batch N                          set process/thread priority : 0-normal, 1-medium, 2-high, 3-realtime
                                        (default: 0)
--poll-batch <0|1>                      use polling to wait for work (default: same as --poll)
-c,    --ctx-size N                     size of the prompt context (default: 0, 0 = loaded from model)
                                        (env: LLAMA_ARG_CTX_SIZE)
-n,    --predict, --n-predict N         number of tokens to predict (default: -1, -1 = infinity, -2 = until
                                        context filled)
                                        (env: LLAMA_ARG_N_PREDICT)
-b,    --batch-size N                   logical maximum batch size (default: 2048)
                                        (env: LLAMA_ARG_BATCH)
-ub,   --ubatch-size N                  physical maximum batch size (default: 512)
                                        (env: LLAMA_ARG_UBATCH)
--keep N                                number of tokens to keep from the initial prompt (default: 0, -1 =
                                        all)
-fa,   --flash-attn                     enable Flash Attention (default: disabled)
                                        (env: LLAMA_ARG_FLASH_ATTN)
-p,    --prompt PROMPT                  prompt to start generation with
-f,    --file FNAME                     a file containing the prompt (default: none)
-bf,   --binary-file FNAME              binary file containing the prompt (default: none)
-e,    --escape                         process escapes sequences (\n, \r, \t, \', \", \\) (default: true)
--no-escape                             do not process escape sequences
--rope-scaling {none,linear,yarn}       RoPE frequency scaling method, defaults to linear unless specified by
                                        the model
--rope-scale N                          RoPE context scaling factor, expands context by a factor of N
--rope-freq-base N                      RoPE base frequency, used by NTK-aware scaling (default: loaded from
                                        model)
--rope-freq-scale N                     RoPE frequency scaling factor, expands context by a factor of 1/N
--yarn-orig-ctx N                       YaRN: original context size of model (default: 0 = model training
                                        context size)
--yarn-ext-factor N                     YaRN: extrapolation mix factor (default: -1.0, 0.0 = full
                                        interpolation)
--yarn-attn-factor N                    YaRN: scale sqrt(t) or attention magnitude (default: 1.0)
--yarn-beta-slow N                      YaRN: high correction dim or alpha (default: 1.0)
--yarn-beta-fast N                      YaRN: low correction dim or beta (default: 32.0)
-gan,  --grp-attn-n N                   group-attention factor (default: 1)
-gaw,  --grp-attn-w N                   group-attention width (default: 512.0)
-dkvc, --dump-kv-cache                  verbose print of the KV cache
-nkvo, --no-kv-offload                  disable KV offload
-ctk,  --cache-type-k TYPE              KV cache data type for K (default: f16)
-ctv,  --cache-type-v TYPE              KV cache data type for V (default: f16)
-dt,   --defrag-thold N                 KV cache defragmentation threshold (default: -1.0, < 0 - disabled)
                                        (env: LLAMA_ARG_DEFRAG_THOLD)
-np,   --parallel N                     number of parallel sequences to decode (default: 1)
--mlock                                 force system to keep model in RAM rather than swapping or compressing
--no-mmap                               do not memory-map model (slower load but may reduce pageouts if not
                                        using mlock)
--numa TYPE                             attempt optimizations that help on some NUMA systems
                                        - distribute: spread execution evenly over all nodes
                                        - isolate: only spawn threads on CPUs on the node that execution
                                        started on
                                        - numactl: use the CPU map provided by numactl
                                        if run without this previously, it is recommended to drop the system
                                        page cache before using this
                                        see https://github.com/ggerganov/llama.cpp/issues/1437
-ngl,  --gpu-layers, --n-gpu-layers N   number of layers to store in VRAM
                                        (env: LLAMA_ARG_N_GPU_LAYERS)
-sm,   --split-mode {none,layer,row}    how to split the model across multiple GPUs, one of:
                                        - none: use one GPU only
                                        - layer (default): split layers and KV across GPUs
                                        - row: split rows across GPUs
-ts,   --tensor-split N0,N1,N2,...      fraction of the model to offload to each GPU, comma-separated list of
                                        proportions, e.g. 3,1
-mg,   --main-gpu INDEX                 the GPU to use for the model (with split-mode = none), or for
                                        intermediate results and KV (with split-mode = row) (default: 0)
--check-tensors                         check model tensor data for invalid values (default: false)
--override-kv KEY=TYPE:VALUE            advanced option to override model metadata by key. may be specified
                                        multiple times.
                                        types: int, float, bool, str. example: --override-kv
                                        tokenizer.ggml.add_bos_token=bool:false
--lora FNAME                            path to LoRA adapter (can be repeated to use multiple adapters)
--lora-scaled FNAME SCALE               path to LoRA adapter with user defined scaling (can be repeated to use
                                        multiple adapters)
--control-vector FNAME                  add a control vector
                                        note: this argument can be repeated to add multiple control vectors
--control-vector-scaled FNAME SCALE     add a control vector with user defined scaling SCALE
                                        note: this argument can be repeated to add multiple scaled control
                                        vectors
--control-vector-layer-range START END
                                        layer range to apply the control vector(s) to, start and end inclusive
-m,    --model FNAME                    model path (default: `models/$filename` with filename from `--hf-file`
                                        or `--model-url` if set, otherwise models/7B/ggml-model-f16.gguf)
                                        (env: LLAMA_ARG_MODEL)
-mu,   --model-url MODEL_URL            model download url (default: unused)
                                        (env: LLAMA_ARG_MODEL_URL)
-hfr,  --hf-repo REPO                   Hugging Face model repository (default: unused)
                                        (env: LLAMA_ARG_HF_REPO)
-hff,  --hf-file FILE                   Hugging Face model file (default: unused)
                                        (env: LLAMA_ARG_HF_FILE)
-hft,  --hf-token TOKEN                 Hugging Face access token (default: value from HF_TOKEN environment
                                        variable)
                                        (env: HF_TOKEN)
-ld,   --logdir LOGDIR                  path under which to save YAML logs (no logging if unset)
--log-test                              Log test
--log-disable                           Log disable
--log-enable                            Log enable
--log-new                               Log new
--log-append                            Log append
--log-file FNAME                        Log file
```

----- sampling params -----
```
--samplers SAMPLERS                     samplers that will be used for generation in the order, separated by
                                        ';'
                                        (default: top_k;tfs_z;typ_p;top_p;min_p;temperature)
-s,    --seed SEED                      RNG seed (default: 4294967295, use random seed for 4294967295)
--sampling-seq SEQUENCE                 simplified sequence for samplers that will be used (default: kfypmt)
--ignore-eos                            ignore end of stream token and continue generating (implies
                                        --logit-bias EOS-inf)
--penalize-nl                           penalize newline tokens (default: false)
--temp N                                temperature (default: 0.8)
--top-k N                               top-k sampling (default: 40, 0 = disabled)
--top-p N                               top-p sampling (default: 0.9, 1.0 = disabled)
--min-p N                               min-p sampling (default: 0.1, 0.0 = disabled)
--tfs N                                 tail free sampling, parameter z (default: 1.0, 1.0 = disabled)
--typical N                             locally typical sampling, parameter p (default: 1.0, 1.0 = disabled)
--repeat-last-n N                       last n tokens to consider for penalize (default: 64, 0 = disabled, -1
                                        = ctx_size)
--repeat-penalty N                      penalize repeat sequence of tokens (default: 1.0, 1.0 = disabled)
--presence-penalty N                    repeat alpha presence penalty (default: 0.0, 0.0 = disabled)
--frequency-penalty N                   repeat alpha frequency penalty (default: 0.0, 0.0 = disabled)
--dynatemp-range N                      dynamic temperature range (default: 0.0, 0.0 = disabled)
--dynatemp-exp N                        dynamic temperature exponent (default: 1.0)
--mirostat N                            use Mirostat sampling.
                                        Top K, Nucleus, Tail Free and Locally Typical samplers are ignored if
                                        used.
                                        (default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)
--mirostat-lr N                         Mirostat learning rate, parameter eta (default: 0.1)
--mirostat-ent N                        Mirostat target entropy, parameter tau (default: 5.0)
-l,    --logit-bias TOKEN_ID(+/-)BIAS   modifies the likelihood of token appearing in the completion,
                                        i.e. `--logit-bias 15043+1` to increase likelihood of token ' Hello',
                                        or `--logit-bias 15043-1` to decrease likelihood of token ' Hello'
--grammar GRAMMAR                       BNF-like grammar to constrain generations (see samples in grammars/
                                        dir) (default: '')
--grammar-file FNAME                    file to read grammar from
-j,    --json-schema SCHEMA             JSON schema to constrain generations (https://json-schema.org/), e.g.
                                        `{}` for any JSON object
                                        For schemas w/ external $refs, use --grammar +
                                        example/json_schema_to_grammar.py instead
```

----- example-specific params -----
```
--chunks N                              max number of chunks to process (default: -1, -1 = all)
--context-file FNAME                    file to load context from (repeat to specify multiple files)
--chunk-size N                          minimum length of embedded text chunks (default: 64)
--chunk-separator STRING                separator between chunks (default: '
                                        ')
```
example usage:
```
    .\llama-retrieval.exe --model models/7B/ggml-model-q3.gguf --top-k 3 --context-file README.md --context-file License --chunk-size 100 --chunk-separator .
```

## llama-save-load-state.exe

## llama-server.exe
To start the server with minimal options,

    .\llama-server.exe -m models/7B/ggml-model-q3.gguf -p 8080

must include a model.

----- common params -----
```
-h,    --help, --usage                  print usage and exit
--version                               show version and build info
-v,    --verbose                        print verbose information
--verbosity N                           set specific verbosity level (default: 0)
-t,    --threads N                      number of threads to use during generation (default: -1)
                                        (env: LLAMA_ARG_THREADS)
-tb,   --threads-batch N                number of threads to use during batch and prompt processing (default:
                                        same as --threads)
-C,    --cpu-mask M                     CPU affinity mask: arbitrarily long hex. Complements cpu-range
                                        (default: "")
-Cr,   --cpu-range lo-hi                range of CPUs for affinity. Complements --cpu-mask
--cpu-strict <0|1>                      use strict CPU placement (default: 0)
--prio N                                set process/thread priority : 0-normal, 1-medium, 2-high, 3-realtime
                                        (default: 0)
--poll <0...100>                        use polling level to wait for work (0 - no polling, default: 50)
-Cb,   --cpu-mask-batch M               CPU affinity mask: arbitrarily long hex. Complements cpu-range-batch
                                        (default: same as --cpu-mask)
-Crb,  --cpu-range-batch lo-hi          ranges of CPUs for affinity. Complements --cpu-mask-batch
--cpu-strict-batch <0|1>                use strict CPU placement (default: same as --cpu-strict)
--prio-batch N                          set process/thread priority : 0-normal, 1-medium, 2-high, 3-realtime
                                        (default: 0)
--poll-batch <0|1>                      use polling to wait for work (default: same as --poll)
-c,    --ctx-size N                     size of the prompt context (default: 0, 0 = loaded from model)
                                        (env: LLAMA_ARG_CTX_SIZE)
-n,    --predict, --n-predict N         number of tokens to predict (default: -1, -1 = infinity, -2 = until
                                        context filled)
                                        (env: LLAMA_ARG_N_PREDICT)
-b,    --batch-size N                   logical maximum batch size (default: 2048)
                                        (env: LLAMA_ARG_BATCH)
-ub,   --ubatch-size N                  physical maximum batch size (default: 512)
                                        (env: LLAMA_ARG_UBATCH)
--keep N                                number of tokens to keep from the initial prompt (default: 0, -1 =
                                        all)
-fa,   --flash-attn                     enable Flash Attention (default: disabled)
                                        (env: LLAMA_ARG_FLASH_ATTN)
-p,    --prompt PROMPT                  prompt to start generation with
-f,    --file FNAME                     a file containing the prompt (default: none)
-bf,   --binary-file FNAME              binary file containing the prompt (default: none)
-e,    --escape                         process escapes sequences (\n, \r, \t, \', \", \\) (default: true)
--no-escape                             do not process escape sequences
--rope-scaling {none,linear,yarn}       RoPE frequency scaling method, defaults to linear unless specified by
                                        the model
--rope-scale N                          RoPE context scaling factor, expands context by a factor of N
--rope-freq-base N                      RoPE base frequency, used by NTK-aware scaling (default: loaded from
                                        model)
--rope-freq-scale N                     RoPE frequency scaling factor, expands context by a factor of 1/N
--yarn-orig-ctx N                       YaRN: original context size of model (default: 0 = model training
                                        context size)
--yarn-ext-factor N                     YaRN: extrapolation mix factor (default: -1.0, 0.0 = full
                                        interpolation)
--yarn-attn-factor N                    YaRN: scale sqrt(t) or attention magnitude (default: 1.0)
--yarn-beta-slow N                      YaRN: high correction dim or alpha (default: 1.0)
--yarn-beta-fast N                      YaRN: low correction dim or beta (default: 32.0)
-gan,  --grp-attn-n N                   group-attention factor (default: 1)
-gaw,  --grp-attn-w N                   group-attention width (default: 512.0)
-dkvc, --dump-kv-cache                  verbose print of the KV cache
-nkvo, --no-kv-offload                  disable KV offload
-ctk,  --cache-type-k TYPE              KV cache data type for K (default: f16)
-ctv,  --cache-type-v TYPE              KV cache data type for V (default: f16)
-dt,   --defrag-thold N                 KV cache defragmentation threshold (default: -1.0, < 0 - disabled)
                                        (env: LLAMA_ARG_DEFRAG_THOLD)
-np,   --parallel N                     number of parallel sequences to decode (default: 1)
--mlock                                 force system to keep model in RAM rather than swapping or compressing
--no-mmap                               do not memory-map model (slower load but may reduce pageouts if not
                                        using mlock)
--numa TYPE                             attempt optimizations that help on some NUMA systems
                                        - distribute: spread execution evenly over all nodes
                                        - isolate: only spawn threads on CPUs on the node that execution
                                        started on
                                        - numactl: use the CPU map provided by numactl
                                        if run without this previously, it is recommended to drop the system
                                        page cache before using this
                                        see https://github.com/ggerganov/llama.cpp/issues/1437
-ngl,  --gpu-layers, --n-gpu-layers N   number of layers to store in VRAM
                                        (env: LLAMA_ARG_N_GPU_LAYERS)
-sm,   --split-mode {none,layer,row}    how to split the model across multiple GPUs, one of:
                                        - none: use one GPU only
                                        - layer (default): split layers and KV across GPUs
                                        - row: split rows across GPUs
-ts,   --tensor-split N0,N1,N2,...      fraction of the model to offload to each GPU, comma-separated list of
                                        proportions, e.g. 3,1
-mg,   --main-gpu INDEX                 the GPU to use for the model (with split-mode = none), or for
                                        intermediate results and KV (with split-mode = row) (default: 0)
--check-tensors                         check model tensor data for invalid values (default: false)
--override-kv KEY=TYPE:VALUE            advanced option to override model metadata by key. may be specified
                                        multiple times.
                                        types: int, float, bool, str. example: --override-kv
                                        tokenizer.ggml.add_bos_token=bool:false
--lora FNAME                            path to LoRA adapter (can be repeated to use multiple adapters)
--lora-scaled FNAME SCALE               path to LoRA adapter with user defined scaling (can be repeated to use
                                        multiple adapters)
--control-vector FNAME                  add a control vector
                                        note: this argument can be repeated to add multiple control vectors
--control-vector-scaled FNAME SCALE     add a control vector with user defined scaling SCALE
                                        note: this argument can be repeated to add multiple scaled control
                                        vectors
--control-vector-layer-range START END
                                        layer range to apply the control vector(s) to, start and end inclusive
-m,    --model FNAME                    model path (default: `models/$filename` with filename from `--hf-file`
                                        or `--model-url` if set, otherwise models/7B/ggml-model-f16.gguf)
                                        (env: LLAMA_ARG_MODEL)
-mu,   --model-url MODEL_URL            model download url (default: unused)
                                        (env: LLAMA_ARG_MODEL_URL)
-hfr,  --hf-repo REPO                   Hugging Face model repository (default: unused)
                                        (env: LLAMA_ARG_HF_REPO)
-hff,  --hf-file FILE                   Hugging Face model file (default: unused)
                                        (env: LLAMA_ARG_HF_FILE)
-hft,  --hf-token TOKEN                 Hugging Face access token (default: value from HF_TOKEN environment
                                        variable)
                                        (env: HF_TOKEN)
-ld,   --logdir LOGDIR                  path under which to save YAML logs (no logging if unset)
--log-test                              Log test
--log-disable                           Log disable
--log-enable                            Log enable
--log-new                               Log new
--log-append                            Log append
--log-file FNAME                        Log file
```

----- sampling params -----
```
--samplers SAMPLERS                     samplers that will be used for generation in the order, separated by
                                        ';'
                                        (default: top_k;tfs_z;typ_p;top_p;min_p;temperature)
-s,    --seed SEED                      RNG seed (default: 4294967295, use random seed for 4294967295)
--sampling-seq SEQUENCE                 simplified sequence for samplers that will be used (default: kfypmt)
--ignore-eos                            ignore end of stream token and continue generating (implies
                                        --logit-bias EOS-inf)
--penalize-nl                           penalize newline tokens (default: false)
--temp N                                temperature (default: 0.8)
--top-k N                               top-k sampling (default: 40, 0 = disabled)
--top-p N                               top-p sampling (default: 0.9, 1.0 = disabled)
--min-p N                               min-p sampling (default: 0.1, 0.0 = disabled)
--tfs N                                 tail free sampling, parameter z (default: 1.0, 1.0 = disabled)
--typical N                             locally typical sampling, parameter p (default: 1.0, 1.0 = disabled)
--repeat-last-n N                       last n tokens to consider for penalize (default: 64, 0 = disabled, -1
                                        = ctx_size)
--repeat-penalty N                      penalize repeat sequence of tokens (default: 1.0, 1.0 = disabled)
--presence-penalty N                    repeat alpha presence penalty (default: 0.0, 0.0 = disabled)
--frequency-penalty N                   repeat alpha frequency penalty (default: 0.0, 0.0 = disabled)
--dynatemp-range N                      dynamic temperature range (default: 0.0, 0.0 = disabled)
--dynatemp-exp N                        dynamic temperature exponent (default: 1.0)
--mirostat N                            use Mirostat sampling.
                                        Top K, Nucleus, Tail Free and Locally Typical samplers are ignored if
                                        used.
                                        (default: 0, 0 = disabled, 1 = Mirostat, 2 = Mirostat 2.0)
--mirostat-lr N                         Mirostat learning rate, parameter eta (default: 0.1)
--mirostat-ent N                        Mirostat target entropy, parameter tau (default: 5.0)
-l,    --logit-bias TOKEN_ID(+/-)BIAS   modifies the likelihood of token appearing in the completion,
                                        i.e. `--logit-bias 15043+1` to increase likelihood of token ' Hello',
                                        or `--logit-bias 15043-1` to decrease likelihood of token ' Hello'
--grammar GRAMMAR                       BNF-like grammar to constrain generations (see samples in grammars/
                                        dir) (default: '')
--grammar-file FNAME                    file to read grammar from
-j,    --json-schema SCHEMA             JSON schema to constrain generations (https://json-schema.org/), e.g.
                                        `{}` for any JSON object
                                        For schemas w/ external $refs, use --grammar +
                                        example/json_schema_to_grammar.py instead
```

----- example-specific params -----
```
-sp,   --special                        special tokens output enabled (default: false)
--spm-infill                            use Suffix/Prefix/Middle pattern for infill (instead of
                                        Prefix/Suffix/Middle) as some models prefer this. (default: disabled)
-cb,   --cont-batching                  enable continuous batching (a.k.a dynamic batching) (default: enabled)
                                        (env: LLAMA_ARG_CONT_BATCHING)
-nocb, --no-cont-batching               disable continuous batching
                                        (env: LLAMA_ARG_NO_CONT_BATCHING)
-a,    --alias STRING                   set alias for model name (to be used by REST API)
--host HOST                             ip address to listen (default: 127.0.0.1)
                                        (env: LLAMA_ARG_HOST)
--port PORT                             port to listen (default: 8080)
                                        (env: LLAMA_ARG_PORT)
--path PATH                             path to serve static files from (default: )
--embedding, --embeddings               restrict to only support embedding use case; use only with dedicated
                                        embedding models (default: disabled)
                                        (env: LLAMA_ARG_EMBEDDINGS)
--api-key KEY                           API key to use for authentication (default: none)
                                        (env: LLAMA_API_KEY)
--api-key-file FNAME                    path to file containing API keys (default: none)
--ssl-key-file FNAME                    path to file a PEM-encoded SSL private key
--ssl-cert-file FNAME                   path to file a PEM-encoded SSL certificate
-to,   --timeout N                      server read/write timeout in seconds (default: 600)
--threads-http N                        number of threads used to process HTTP requests (default: -1)
                                        (env: LLAMA_ARG_THREADS_HTTP)
-spf,  --system-prompt-file FNAME       set a file to load a system prompt (initial prompt of all slots), this
                                        is useful for chat applications
--log-format {text, json}               log output format: json or text (default: json)
--metrics                               enable prometheus compatible metrics endpoint (default: disabled)
                                        (env: LLAMA_ARG_ENDPOINT_METRICS)
--no-slots                              disables slots monitoring endpoint (default: enabled)
                                        (env: LLAMA_ARG_NO_ENDPOINT_SLOTS)
--slot-save-path PATH                   path to save slot kv cache (default: disabled)
--chat-template JINJA_TEMPLATE          set custom jinja chat template (default: template taken from model's
                                        metadata)
                                        if suffix/prefix are specified, template will be disabled
                                        only commonly used templates are accepted:
                                        https://github.com/ggerganov/llama.cpp/wiki/Templates-supported-by-llama_chat_apply_template
                                        (env: LLAMA_ARG_CHAT_TEMPLATE)
-sps,  --slot-prompt-similarity SIMILARITY
                                        how much the prompt of a request must match the prompt of a slot in
                                        order to use that slot (default: 0.50, 0.0 = disabled)
--lora-init-without-apply               load LoRA adapters without applying them (apply later via POST
                                        /lora-adapters) (default: disabled)
```
For a typical `llama-server`, which could be set up for serving LLaMA models for inference, embeddings, or other tasks, you can structure the routes based on common functionalities needed in a Retrieval-Augmented Generation (RAG) system or API-based LLM server. Below is a sample outline of possible routes:

### **Health Status**
   - **GET `/health`**: Check health
     - **Response**: "ok" status.
       ```json
       {
         "status": "ok"
       }
       ```

These routes would cover the typical functions of a `llama-server` setup, providing endpoints for inference, embeddings, model management, and additional features like retrieval and quantization. Would you like to add or modify any specific routes for your server setup?
## llama-simple.exe

## llama-speculative.exe

## llama-tokenize.exe

## llama-vdot.exe
