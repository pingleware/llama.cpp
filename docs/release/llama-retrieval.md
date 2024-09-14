# llama-retrieval.exe
----- common params -----

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


----- sampling params -----

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


----- example-specific params -----

--chunks N                              max number of chunks to process (default: -1, -1 = all)
--context-file FNAME                    file to load context from (repeat to specify multiple files)
--chunk-size N                          minimum length of embedded text chunks (default: 64)
--chunk-separator STRING                separator between chunks (default: '
                                        ')

example usage:

    .\llama-retrieval.exe --model ./models/bge-base-en-v1.5-f16.gguf --top-k 3 --context-file README.md --context-file License --chunk-size 100 --chunk-separator .

.\llama-retrieval.exe --model models\ggml-model-q3.gguf --threads 4 --cpu-range 0-1 --ctx-size 512 --batch-size 256 --cpu-strict 1 --prio 1 --chunk-size 100 --chunk-separator " "

.\llama-retrieval.exe --model models\ggml-model-q3.gguf --threads 4 --cpu-mask 3 --ctx-size 512 --batch-size 256 --cpu-strict 1 --prio 1 --chunk-size 100 --chunk-separator " " --context-file path_to_context_file1.txt --context-file path_to_context_file2.txt
