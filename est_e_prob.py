# A base de dados descreve o tempo medio semanal que os alunos do Cin passam no celular
# Os dados são quantitativos e contínuos

dataBase = [4.581, 6.663, 7.531, 5.577, 5.147, 4.67, 6.036, 3.882, 3.88, 5.248,
            4.189, 5.86, 6.13, 7.6, 6.441, 4.429, 6.913, 3.355, 5.52, 3.277,
            5.781, 4.678, 4.166, 5.856, 6.467, 4.984, 2.571, 3.125, 6.627, 5.838,
            5.724, 5.476, 6.191, 1.494, 2.73, 4.572, 5.97, 7.217, 5.382, 4.137,
            6.413, 4.653, 6.829, 5.202, 5.3, 6.225, 5.79, 5.3, 6.883, 4.774,
            3.699, 6.844, 7.729, 4.447, 4.567, 4.566, 7.162, 6.937, 7.493, 3.523,
            8.343, 4.262, 6.733, 5.973, 4.708, 6.088, 5.621, 4.699, 5.092, 6.239,
            5.321, 4.498, 5.806, 4.795, 5.36, 5.342, 4.845, 7.475, 4.635, 5.08,
            3.606, 4.101, 5.803, 4.352, 6.555, 4.815, 5.335, 6.315, 5.631, 6.579,
            4.866, 4.462, 6.45, 4.756, 5.455, 6.318, 6.257, 4.383, 3.086, 3.007,
            5.497, 3.586, 4.919, 3.49, 4.667, 3.79, 4.328, 4.455, 2.786, 7.497,
            4.818, 3.972, 6.182, 6.63, 5.011, 4.643, 6.146, 6.332, 4.779, 6.443,
            6.579, 6.364, 4.765, 6.468, 4.67, 5.91, 4.65, 5.304, 6.623, 5.64,
            6.347, 4.202, 3.714, 6.043, 6.057, 4.842, 5.473, 6.418, 5.331, 4.558,
            5.897, 4.75, 4.538, 4.472, 3.121, 3.63, 5.858, 3.642, 3.522, 4.718,
            4.703, 6.023, 4.741, 6.296, 5.801, 3.377, 3.622, 5.633, 6.195, 4.879,
            5.549, 4.28, 6.094, 4.912, 6.727, 6.631, 5.756, 4.717, 5.526, 3.395,
            5.223, 5.359, 4.329, 4.517, 6.214, 3.084, 5.848, 4.899, 6.435, 5.243,
            5.45, 3.468, 6.732, 3.136, 4.526, 5.86, 4.966, 5.93, 5.364, 4.952,
            6.327, 5.997, 5.185, 5.867, 3.746, 5.029, 5.375, 5.361, 5.069, 6.074,
            6.365, 7.16, 5.366, 6.719, 5.411, 4.35, 5.821, 4.496, 5.795, 4.579,
            3.832, 3.567, 5.536, 3.69, 5.364, 5.583, 5.014, 4.642, 5.371, 5.2,
            5.309, 4.208, 4.062, 4.135, 5.964, 3.494, 5.423, 6.681, 6.053, 4.581,
            2.464, 5.715, 6.616, 2.364, 6.405, 4.711, 5.932, 5.275, 4.888, 5.007,
            3.796, 4.574, 5.539, 3.887, 5.784, 4.685, 5.255, 5.298, 3.394, 5.217,
            4.71, 5.266, 4.775, 5.582, 6.583, 4.854, 5.621, 3.194, 6.038, 3.291,
            5.829, 4.504, 6.45, 4.829, 4.62, 6.225, 6.583, 6.255, 4.274, 4.336,
            7.292, 5.171, 3.862, 5.091, 5.212, 4.934, 6.236, 5.173, 4.485, 6.273,
            3.667, 4.609, 5.635, 5.336, 5.9, 4.114, 6.106, 4.963, 5.528, 7.651,
            4.849, 3.939, 5.067, 2.883, 6.946, 4.49, 3.941, 4.81, 4.836, 4.708,
            4.779, 6.643, 7.963, 6.064, 5.418, 5.032, 5.241, 6.163, 5.965, 5.335,
            5.63, 6.415, 4.482, 4.402, 4.038, 5.474, 5.333, 7.112, 5.626, 6.237,
            5.432, 3.754, 5.33, 5.766, 6.077, 3.744, 5.658, 5.125, 4.036, 3.511,
            4.47, 7.086, 7.584, 6.332, 4.484, 4.476, 4.554, 6.041, 5.73, 5.549,
            4.236, 3.044, 5.267, 4.849, 5.482, 4.781, 6.322, 3.342, 4.791, 6.466,
            3.815, 5.336, 5.456, 6.66, 5.463, 6.004, 4.51, 4.725, 3.317, 3.926,
            3.015, 5.259, 3.139, 5.454, 5.26, 4.137, 5.773, 3.597, 4.973, 7.122, 
            6.243, 5.513, 6.117, 4.057, 4.918, 5.58, 6.665, 5.486, 5.464, 1.415,
            4.315, 7.919, 6.573, 5.131, 5.672, 6.174, 5.198, 4.311, 6.229, 4.273,
            4.249, 7.542, 6.682, 5.357, 4.326, 5.327, 6.274, 6.477, 5.532, 5.963,
            5.371, 5.604, 4.347, 3.119, 6.773, 5.59, 6.928, 5.729, 5.078, 4.916,
            5.238, 5.957, 6.829, 6.078, 3.558, 5.416, 5.077, 5.039, 4.994, 4.339,
            6.095, 5.552, 6.411, 4.099, 6.704, 3.185, 2.877, 5.512, 5.026, 5.843,
            5.478, 6.284, 6.161, 5.992, 6.682, 3.763, 5.645, 5.1, 5.916, 4.682,
            6.064, 5.379, 8.89, 4.978, 6.432, 5.472, 3.277, 5.804, 5.644, 7.912,
            2.848, 7.397, 4.195, 6.6, 3.511, 5.673, 5.434, 4.978, 6.096, 5.133,
            5.556, 4.502, 5.368, 2.062, 4.479, 5.255, 6.241, 4.818, 5.228, 5.623,
            7.226, 6.209, 4.183, 7.42, 4.077, 3.208, 3.402, 5.21, 5.828, 5.708,
            5.474, 6.5, 3.906, 5.888, 4.849, 3.967, 6.516, 6.665, 4.497, 6.271,
            4.914, 5.39, 5.273, 5.066, 4.547, 8.395, 5.702, 4.254, 5.626, 7.632,
            2.508, 4.461, 5.834, 6.515, 5.345, 4.156, 4.934, 6.48, 5.878, 3.527,
            6.807, 5.785, 6.646, 5.665, 6.021, 6.344, 7.267, 5.257, 4.548, 4.322,
            3.126, 5.589, 6.342, 6.109, 4.038, 3.422, 5.639, 4.248, 5.86, 3.388,
            2.639, 6.443, 5.073, 6.675, 5.306, 5.149, 3.353, 5.121, 4.969, 5.263,
            6.741, 3.76, 5.034, 4.607, 6.143, 5.366, 4.592, 5.035, 4.344, 5.128,
            6.32, 5.875, 6.695, 6.612, 6.021, 4.167, 6.471, 5.371, 4.913, 6.217,
            3.649, 3.774, 6.479, 5.928, 6.912, 5.956, 4.413, 6.071, 4.517, 5.214,
            4.377, 3.336, 5.401, 5.618, 5.005, 4.865, 5.893, 5.03, 5.302, 3.17,
            6.254, 6.7, 5.643, 3.753, 5.492, 4.192, 3.592, 5.51, 4.62, 5.929,
            4.862, 7.129, 3.828, 5.928, 5.5, 3.622, 4.62, 4.417, 5.384, 5.678,
            3.768, 4.694, 2.759, 3.655, 5.953, 3.918, 5.017, 7.09, 6.558, 5.475,
            5.572, 4.452, 7.081, 7.718, 7.386, 7.213, 6.208, 5.383, 5.686, 6.283,
            3.894, 5.591, 5.772, 3.856, 4.823, 5.014, 3.735, 4.865, 6.082, 4.748,
            5.805, 5.509, 4.405, 2.486, 4.722, 3.406, 4.106, 4.112, 5.036, 4.321,
            4.746, 5.425, 3.626, 4.075, 4.404, 6.017, 4.92, 3.771, 7.34, 3.825,
            5.152, 5.372, 7.824, 3.509, 5.601, 5.529, 6.004, 4.819, 5.0, 5.972,
            6.54, 5.035, 5.44, 5.573, 5.404, 5.457, 7.105, 6.41, 8.134, 5.798,
            6.261, 6.255, 5.908, 4.257, 4.504, 5.735, 5.415, 5.007, 4.74, 5.175,
            6.062, 4.587, 6.529, 4.288, 5.374, 5.599, 6.192, 4.963, 4.406, 5.172,
            5.892, 5.361, 4.234, 4.569, 6.292, 2.745, 6.789, 2.798, 5.628, 4.769,
            4.397, 5.275, 5.863, 4.548, 7.197, 5.025, 2.232, 6.049, 4.329, 4.467,
            5.52, 5.394, 5.77, 6.124, 6.542, 4.188, 6.745, 4.012, 5.081, 5.209,
            5.157, 3.066, 5.002, 3.265, 6.704, 3.998, 5.841, 4.541, 6.77, 6.238,
            7.181, 5.002, 5.724, 5.252, 6.019, 5.841, 2.577, 4.904, 5.987, 5.299,
            5.666, 7.081, 5.384, 6.623, 4.558, 4.432, 8.453, 4.722, 3.284, 6.12,
            3.945, 4.97, 5.994, 3.426, 4.443, 4.04, 4.893, 4.394, 4.983, 4.383,
            6.719, 4.691, 4.78, 5.553, 5.535, 4.424, 3.929, 5.166, 4.236, 5.316,
            5.085, 6.45, 5.666, 5.069, 5.903, 4.766, 5.067, 2.985, 3.445, 5.081,
            5.722, 4.245, 2.962, 5.434, 4.324, 5.801, 7.035, 3.074, 7.031, 3.028,
            6.224, 5.377, 7.057, 4.886, 5.021, 5.625, 4.296, 6.997, 5.367, 4.298,
            4.026, 7.652, 5.048, 5.524, 4.259, 3.89, 6.123, 4.998, 6.914, 5.599,
            6.796, 6.531, 6.489, 5.677, 5.124, 5.383, 4.184, 3.901, 5.766, 5.631,
            7.479, 3.974, 7.191, 6.256, 7.105, 6.101, 5.001, 5.72, 4.022, 4.125,
            5.695, 4.997, 4.073, 3.996, 4.593, 4.343, 5.37, 6.378, 6.622, 4.207,
            3.932, 5.36, 7.203, 5.44, 5.149, 4.29, 6.116, 4.758, 7.282, 4.522, 6.054,
            8.318, 6.716, 5.267, 5.653, 4.029, 5.056, 5.65, 4.648, 7.077, 6.249,
            3.305, 3.986, 5.282, 5.048, 4.932, 5.428, 6.46, 5.578, 4.576, 2.664,
            6.667, 5.787, 4.775, 5.768, 4.268, 4.566, 3.625, 6.727, 4.097, 4.654,
            3.461, 3.998, 7.097, 6.325, 4.4, 5.403, 5.501, 5.099, 4.289, 2.403,
            6.47, 4.674, 3.488, 6.916, 8.483, 3.767, 5.691, 5.428, 4.623, 6.99,
            5.076, 6.853, 5.19, 5.496, 6.711, 4.667, 5.742, 3.525, 6.635, 5.047,
            6.77, 6.38, 3.641, 4.358, 3.698, 7.616, 5.789, 6.77, 5.336, 5.655,
            4.674, 6.657, 4.783, 3.789, 4.948, 4.583, 5.722, 6.54, 3.589, 6.104,
            5.398, 4.734, 4.927, 5.784, 5.852, 4.667, 2.417, 5.225, 5.653, 8.168,
            3.692, 6.29, 5.12, 3.609, 5.457, 5.58, 7.191, 5.632, 6.506, 4.461,
            7.268, 4.15, 4.047, 5.175, 4.825, 7.46, 5.851, 3.963, 4.831, 4.004,
            6.109, 3.475, 4.721, 4.375, 3.708, 4.941, 4.27, 3.352, 3.176, 6.757,
            6.203, 5.946, 3.846, 5.535, 6.044, 4.161, 5.1, 5.775, 2.668, 3.715,
            4.904, 6.204, 3.999, 7.285, 4.828, 5.054, 5.755, 5.653, 6.005, 3.603,
            4.929, 3.611, 4.326, 4.058, 5.492, 4.676, 3.835, 3.292, 7.251
]

sortedDataBase = [1.415, 1.494, 2.062, 2.232, 2.364, 2.403, 2.417, 2.464, 2.486, 2.508, 
                  2.571, 2.577, 2.639, 2.664, 2.668, 2.73, 2.745, 2.759, 2.786, 2.798, 
                  2.848, 2.877, 2.883, 2.962, 2.985, 3.007, 3.015, 3.028, 3.044, 3.066, 
                  3.074, 3.084, 3.086, 3.119, 3.121, 3.125, 3.126, 3.136, 3.139, 3.17, 
                  3.176, 3.185, 3.194, 3.208, 3.265, 3.277, 3.277, 3.284, 3.291, 3.292, 
                  3.305, 3.317, 3.336, 3.342, 3.352, 3.353, 3.355, 3.377, 3.388, 3.394, 
                  3.395, 3.402, 3.406, 3.422, 3.426, 3.445, 3.461, 3.468, 3.475, 3.488, 
                  3.49, 3.494, 3.509, 3.511, 3.511, 3.522, 3.523, 3.525, 3.527, 3.558, 
                  3.567, 3.586, 3.589, 3.592, 3.597, 3.603, 3.606, 3.609, 3.611, 3.622, 
                  3.622, 3.625, 3.626, 3.63, 3.641, 3.642, 3.649, 3.655, 3.667, 3.69, 
                  3.692, 3.698, 3.699, 3.708, 3.714, 3.715, 3.735, 3.744, 3.746, 3.753, 
                  3.754, 3.76, 3.763, 3.767, 3.768, 3.771, 3.774, 3.789, 3.79, 3.796, 
                  3.815, 3.825, 3.828, 3.832, 3.835, 3.846, 3.856, 3.862, 3.88, 3.882, 
                  3.887, 3.89, 3.894, 3.901, 3.906, 3.918, 3.926, 3.929, 3.932, 3.939, 
                  3.941, 3.945, 3.963, 3.967, 3.972, 3.974, 3.986, 3.996, 3.998, 3.998, 
                  3.999, 4.004, 4.012, 4.022, 4.026, 4.029, 4.036, 4.038, 4.038, 4.04, 
                  4.047, 4.057, 4.058, 4.062, 4.073, 4.075, 4.077, 4.097, 4.099, 4.101, 
                  4.106, 4.112, 4.114, 4.125, 4.135, 4.137, 4.137, 4.15, 4.156, 4.161, 
                  4.166, 4.167, 4.183, 4.184, 4.188, 4.189, 4.192, 4.195, 4.202, 4.207, 
                  4.208, 4.234, 4.236, 4.236, 4.245, 4.248, 4.249, 4.254, 4.257, 4.259, 
                  4.262, 4.268, 4.27, 4.273, 4.274, 4.28, 4.288, 4.289, 4.29, 4.296, 
                  4.298, 4.311, 4.315, 4.321, 4.322, 4.324, 4.326, 4.326, 4.328, 4.329, 
                  4.329, 4.336, 4.339, 4.343, 4.344, 4.347, 4.35, 4.352, 4.358, 4.375, 
                  4.377, 4.383, 4.383, 4.394, 4.397, 4.4, 4.402, 4.404, 4.405, 4.406, 
                  4.413, 4.417, 4.424, 4.429, 4.432, 4.443, 4.447, 4.452, 4.455, 4.461, 
                  4.461, 4.462, 4.467, 4.47, 4.472, 4.476, 4.479, 4.482, 4.484, 4.485, 
                  4.49, 4.496, 4.497, 4.498, 4.502, 4.504, 4.504, 4.51, 4.517, 4.517, 
                  4.522, 4.526, 4.538, 4.541, 4.547, 4.548, 4.548, 4.554, 4.558, 4.558, 
                  4.566, 4.566, 4.567, 4.569, 4.572, 4.574, 4.576, 4.579, 4.581, 4.581, 
                  4.583, 4.587, 4.592, 4.593, 4.607, 4.609, 4.62, 4.62, 4.62, 4.623, 
                  4.635, 4.642, 4.643, 4.648, 4.65, 4.653, 4.654, 4.667, 4.667, 4.667, 
                  4.67, 4.67, 4.674, 4.674, 4.676, 4.678, 4.682, 4.685, 4.691, 4.694, 
                  4.699, 4.703, 4.708, 4.708, 4.71, 4.711, 4.717, 4.718, 4.721, 4.722, 
                  4.722, 4.725, 4.734, 4.74, 4.741, 4.746, 4.748, 4.75, 4.756, 4.758, 
                  4.765, 4.766, 4.769, 4.774, 4.775, 4.775, 4.779, 4.779, 4.78, 4.781, 
                  4.783, 4.791, 4.795, 4.81, 4.815, 4.818, 4.818, 4.819, 4.823, 4.825, 
                  4.828, 4.829, 4.831, 4.836, 4.842, 4.845, 4.849, 4.849, 4.849, 4.854, 
                  4.862, 4.865, 4.865, 4.866, 4.879, 4.886, 4.888, 4.893, 4.899, 4.904, 
                  4.904, 4.912, 4.913, 4.914, 4.916, 4.918, 4.919, 4.92, 4.927, 4.929, 
                  4.932, 4.934, 4.934, 4.941, 4.948, 4.952, 4.963, 4.963, 4.966, 4.969, 
                  4.97, 4.973, 4.978, 4.978, 4.983, 4.984, 4.994, 4.997, 4.998, 5.0, 
                  5.001, 5.002, 5.002, 5.005, 5.007, 5.007, 5.011, 5.014, 5.014, 5.017, 
                  5.021, 5.025, 5.026, 5.029, 5.03, 5.032, 5.034, 5.035, 5.035, 5.036, 
                  5.039, 5.047, 5.048, 5.048, 5.054, 5.056, 5.066, 5.067, 5.067, 5.069, 
                  5.069, 5.073, 5.076, 5.077, 5.078, 5.08, 5.081, 5.081, 5.085, 5.091, 
                  5.092, 5.099, 5.1, 5.1, 5.12, 5.121, 5.124, 5.125, 5.128, 5.131, 5.133, 
                  5.147, 5.149, 5.149, 5.152, 5.157, 5.166, 5.171, 5.172, 5.173, 5.175, 
                  5.175, 5.185, 5.19, 5.198, 5.2, 5.202, 5.209, 5.21, 5.212, 5.214, 
                  5.217, 5.223, 5.225, 5.228, 5.238, 5.241, 5.243, 5.248, 5.252, 5.255, 
                  5.255, 5.257, 5.259, 5.26, 5.263, 5.266, 5.267, 5.267, 5.273, 5.275, 
                  5.275, 5.282, 5.298, 5.299, 5.3, 5.3, 5.302, 5.304, 5.306, 5.309, 
                  5.316, 5.321, 5.327, 5.33, 5.331, 5.333, 5.335, 5.335, 5.336, 5.336, 
                  5.336, 5.342, 5.345, 5.357, 5.359, 5.36, 5.36, 5.361, 5.361, 5.364, 
                  5.364, 5.366, 5.366, 5.367, 5.368, 5.37, 5.371, 5.371, 5.371, 5.372, 
                  5.374, 5.375, 5.377, 5.379, 5.382, 5.383, 5.383, 5.384, 5.384, 5.39, 
                  5.394, 5.398, 5.401, 5.403, 5.404, 5.411, 5.415, 5.416, 5.418, 5.423, 
                  5.425, 5.428, 5.428, 5.432, 5.434, 5.434, 5.44, 5.44, 5.45, 5.454, 
                  5.455, 5.456, 5.457, 5.457, 5.463, 5.464, 5.472, 5.473, 5.474, 5.474, 
                  5.475, 5.476, 5.478, 5.482, 5.486, 5.492, 5.492, 5.496, 5.497, 5.5, 
                  5.501, 5.509, 5.51, 5.512, 5.513, 5.52, 5.52, 5.524, 5.526, 5.528, 
                  5.529, 5.532, 5.535, 5.535, 5.536, 5.539, 5.549, 5.549, 5.552, 5.553, 
                  5.556, 5.572, 5.573, 5.577, 5.578, 5.58, 5.58, 5.582, 5.583, 5.589, 
                  5.59, 5.591, 5.599, 5.599, 5.601, 5.604, 5.618, 5.621, 5.621, 5.623, 
                  5.625, 5.626, 5.626, 5.628, 5.63, 5.631, 5.631, 5.632, 5.633, 5.635, 
                  5.639, 5.64, 5.643, 5.644, 5.645, 5.65, 5.653, 5.653, 5.653, 5.655, 
                  5.658, 5.665, 5.666, 5.666, 5.672, 5.673, 5.677, 5.678, 5.686, 5.691, 
                  5.695, 5.702, 5.708, 5.715, 5.72, 5.722, 5.722, 5.724, 5.724, 5.729, 
                  5.73, 5.735, 5.742, 5.755, 5.756, 5.766, 5.766, 5.768, 5.77, 5.772, 
                  5.773, 5.775, 5.781, 5.784, 5.784, 5.785, 5.787, 5.789, 5.79, 5.795, 
                  5.798, 5.801, 5.801, 5.803, 5.804, 5.805, 5.806, 5.821, 5.828, 5.829, 
                  5.834, 5.838, 5.841, 5.841, 5.843, 5.848, 5.851, 5.852, 5.856, 5.858, 
                  5.86, 5.86, 5.86, 5.863, 5.867, 5.875, 5.878, 5.888, 5.892, 5.893, 
                  5.897, 5.9, 5.903, 5.908, 5.91, 5.916, 5.928, 5.928, 5.929, 5.93, 
                  5.932, 5.946, 5.953, 5.956, 5.957, 5.963, 5.964, 5.965, 5.97, 5.972, 
                  5.973, 5.987, 5.992, 5.994, 5.997, 6.004, 6.004, 6.005, 6.017, 6.019, 
                  6.021, 6.021, 6.023, 6.036, 6.038, 6.041, 6.043, 6.044, 6.049, 6.053, 
                  6.054, 6.057, 6.062, 6.064, 6.064, 6.071, 6.074, 6.077, 6.078, 6.082, 
                  6.088, 6.094, 6.095, 6.096, 6.101, 6.104, 6.106, 6.109, 6.109, 6.116, 
                  6.117, 6.12, 6.123, 6.124, 6.13, 6.143, 6.146, 6.161, 6.163, 6.174, 
                  6.182, 6.191, 6.192, 6.195, 6.203, 6.204, 6.208, 6.209, 6.214, 6.217, 
                  6.224, 6.225, 6.225, 6.229, 6.236, 6.237, 6.238, 6.239, 6.241, 6.243, 
                  6.249, 6.254, 6.255, 6.255, 6.256, 6.257, 6.261, 6.271, 6.273, 6.274, 
                  6.283, 6.284, 6.29, 6.292, 6.296, 6.315, 6.318, 6.32, 6.322, 6.325, 
                  6.327, 6.332, 6.332, 6.342, 6.344, 6.347, 6.364, 6.365, 6.378, 6.38, 
                  6.405, 6.41, 6.411, 6.413, 6.415, 6.418, 6.432, 6.435, 6.441, 6.443, 
                  6.443, 6.45, 6.45, 6.45, 6.46, 6.466, 6.467, 6.468, 6.47, 6.471, 
                  6.477, 6.479, 6.48, 6.489, 6.5, 6.506, 6.515, 6.516, 6.529, 6.531, 
                  6.54, 6.54, 6.542, 6.555, 6.558, 6.573, 6.579, 6.579, 6.583, 6.583,
                  6.6, 6.612, 6.616, 6.622, 6.623, 6.623, 6.627, 6.63, 6.631, 6.635, 
                  6.643, 6.646, 6.657, 6.66, 6.663, 6.665, 6.665, 6.667, 6.675, 6.681, 
                  6.682, 6.682, 6.695, 6.7, 6.704, 6.704, 6.711, 6.716, 6.719, 6.719, 
                  6.727, 6.727, 6.732, 6.733, 6.741, 6.745, 6.757, 6.77, 6.77, 6.77, 
                  6.773, 6.789, 6.796, 6.807, 6.829, 6.829, 6.844, 6.853, 6.883, 6.912, 
                  6.913, 6.914, 6.916, 6.928, 6.937, 6.946, 6.99, 6.997, 7.031, 7.035, 
                  7.057, 7.077, 7.081, 7.081, 7.086, 7.09, 7.097, 7.105, 7.105, 7.112, 
                  7.122, 7.129, 7.16, 7.162, 7.181, 7.191, 7.191, 7.197, 7.203, 7.213, 
                  7.217, 7.226, 7.251, 7.267, 7.268, 7.282, 7.285, 7.292, 7.34, 7.386, 
                  7.397, 7.42, 7.46, 7.475, 7.479, 7.493, 7.497, 7.531, 7.542, 7.584, 
                  7.6, 7.616, 7.632, 7.651, 7.652, 7.718, 7.729, 7.824, 7.912, 7.919, 
                  7.963, 8.134, 8.168, 8.318, 8.343, 8.395, 8.453, 8.483, 8.89
]

somation = 0
for data in sortedDataBase:
    somation += data

avg = somation/len(sortedDataBase)

maxCount = 0
maxData = []
for data in sortedDataBase:
    currentCount = sortedDataBase.count(data)

    if currentCount == 3 and data not in maxData:
        maxCount = currentCount
        maxData.append(data)

    elif currentCount == maxCount:
        erro = 1

varSomation = 0
for data in sortedDataBase:
    x = (data-avg)**2
    varSomation += x

var = varSomation/len(sortedDataBase)
mediana = (sortedDataBase[int((len(sortedDataBase)/2)-1)]+sortedDataBase[int(len(sortedDataBase)/2)])/2

print(f'Media: {avg}\nMediana {mediana}\nModa: {maxData}\nVariancia: {var}\nDesvio padrao: {var**(1/2)}')

# se repetem 3 vezes: [4.62, 4.667, 4.849, 5.336, 5.371, 5.653, 5.86, 6.45, 6.77]