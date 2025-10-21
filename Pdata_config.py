import pandas as pd
import numpy as np

# CONFIGURACIÓN DE COLORES PARA CADA SERIE
COLOR_MAPPING = {
    'R1': '#E41A1C', 'R2': '#4DAF4A', 'R3': '#377EB8',
    'R4': '#984EA3', 'R5': '#FF7F00', 'S': '#FFFF33',
    'P': '#A65628', 'A': '#F781BF', 'B': '#999999',
    'R0': '#8DD3C7',
    'Pesado': '#1f77b4',  # Color para línea Pesado
    'Ligero': '#ff7f0e'   # Color para línea Ligero
}

# CONFIGURACIÓN PRINCIPAL DE GRÁFICAS
CONFIGURACION = {
    # CASO GENERAL 1: Gráficas con datos en rangos específicos (Rho vs Variables)
    'Rho vs Potencia': {
        'tipo': 'general',
        'xlabel': 'Potencia (%)',
        'ylabel': 'Rho (Δk/k)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'rangos': {
                'A': 'B3:C33', 'B': 'D3:E33', 'R1': 'H3:I33',
                'R2': 'J3:K33', 'R3': 'L3:M33', 'P': 'T3:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F3:G33', 'R4': 'N3:O33',
                'R5': 'P3:Q33', 'S': 'R3:S33'
            }
        }
    },
    
    'Fuel Temp vs Rho': {
        'tipo': 'general',
        'xlabel': 'Fuel Temp (Kº)',
        'ylabel': 'Rho (Δk/k)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'rangos': {
                'A': 'B3:C33', 'B': 'D3:E33', 'R1': 'H3:I33',
                'R2': 'J3:K33', 'R3': 'L3:M33', 'P': 'T3:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F3:G33', 'R4': 'N3:O33',
                'R5': 'P3:Q33', 'S': 'R3:S33'
            }
        }
    },
    
    'Mod Temp vs Rho': {
        'tipo': 'general',
        'xlabel': 'Mod Temp (Kº)',
        'ylabel': 'Rho (Δk/k)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'rangos': {
                'A': 'B3:C33', 'B': 'D3:E33', 'R1': 'H3:I33',
                'R2': 'J3:K33', 'R3': 'L3:M33', 'P': 'T3:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F3:G33', 'R4': 'N3:O33',
                'R5': 'P3:Q33', 'S': 'R3:S33'
            }
        }
    },
    
    'Fuel Temp vs Potencia': {
        'tipo': 'general',
        'xlabel': 'Fuel Temp (Kº)',
        'ylabel': 'Potencia (%)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'rangos': {
                'A': 'B3:C33', 'B': 'D3:E33', 'R1': 'H3:I33',
                'R2': 'J3:K33', 'R3': 'L3:M33', 'P': 'T3:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F3:G33', 'R4': 'N3:O33',
                'R5': 'P3:Q33', 'S': 'R3:S33'
            }
        }
    },
    
    'Mod Temp vs Potencia': {
        'tipo': 'general',
        'xlabel': 'Mod Temp (Kº)',
        'ylabel': 'Potencia (%)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'rangos': {
                'A': 'B3:C33', 'B': 'D3:E33', 'R1': 'H3:I33',
                'R2': 'J3:K33', 'R3': 'L3:M33', 'P': 'T3:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F3:G33', 'R4': 'N3:O33',
                'R5': 'P3:Q33', 'S': 'R3:S33'
            }
        }
    },
    
    'Reactividad vs Posición': {
        'tipo': 'general',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Reactividad (Δk/k)',
        'log_scale': True,
        'es_log_opcional': True,
        'Pesado': {
            'rangos': {
                'A': 'B4:C33', 'B': 'D4:E33', 'R1': 'H4:I33',
                'R2': 'J4:K33', 'R3': 'L4:M33', 'P': 'T4:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F4:G33', 'R4': 'N4:O33',
                'R5': 'P4:Q33', 'S': 'R4:S33'
            }
        }
    },
    
    'Periodo vs Posición': {
        'tipo': 'general',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Periodo (s)',
        'log_scale': True,
        'es_log_opcional': True,
        'Pesado': {
            'rangos': {
                'A': 'B4:C33', 'B': 'D4:E33', 'R1': 'H4:I33',
                'R2': 'J4:K33', 'R3': 'L4:M33', 'P': 'T4:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F4:G33', 'R4': 'N4:O33',
                'R5': 'P4:Q33', 'S': 'R4:S33'
            }
        }
    },
    
    'Potencia vs Posición': {
        'tipo': 'general',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Potencia (%)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'rangos': {
                'A': 'B4:C33', 'B': 'D4:E33', 'R1': 'H4:I33',
                'R2': 'J4:K33', 'R3': 'L4:M33', 'P': 'T4:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F4:G33', 'R4': 'N4:O33',
                'R5': 'P4:Q33', 'S': 'R4:S33'
            }
        }
    },
    
    'Fuel Temp vs Posición': {
        'tipo': 'general',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Fuel Temp (Kº)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'rangos': {
                'A': 'B4:C33', 'B': 'D4:E33', 'R1': 'H4:I33',
                'R2': 'J4:K33', 'R3': 'L4:M33', 'P': 'T4:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F4:G33', 'R4': 'N4:O33',
                'R5': 'P4:Q33', 'S': 'R4:S33'
            }
        }
    },
    
    'Mod Temp vs Posición': {
        'tipo': 'general',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Mod Temp (Kº)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'rangos': {
                'A': 'B4:C33', 'B': 'D4:E33', 'R1': 'H4:I33',
                'R2': 'J4:K33', 'R3': 'L4:M33', 'P': 'T4:U33'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'F4:G33', 'R4': 'N4:O33',
                'R5': 'P4:Q33', 'S': 'R4:S33'
            }
        }
    },
    
    # CASOS ESPECIALES: Configuraciones únicas
    'Periodo vs Rho': {
        'tipo': 'especial_periodo',
        'xlabel': 'Rho (Δk/k)',
        'ylabel': 'Periodo (s)',
        'log_scale': True,
        'es_log_opcional': True,
        'Pesado': {
            'rangos': {
                'R1': 'A5:B34', 'R2': 'A38:B67', 'R3': 'A71:B100',
                'P': 'A203:B232', 'A': 'Q5:R34', 'B': 'J38:K67'
            }
        },
        'Ligero': {
            'rangos': {
                'R0': 'J71:K100', 'R4': 'A104:B133',
                'R5': 'A137:B166', 'S': 'A170:B199'
            }
        }
    },
    
    'P. Relativa vs Posición Axial': {
        'tipo': 'especial_potencia',
        'xlabel': 'Potencia Relativa (Watts)',
        'ylabel': 'Posición (cm)',
        'log_scale': False,
        'es_log_opcional': False,
        'Pesado': {
            'usecols': 'B,C,E,I,K,M,U',
            'names': ['Posicion', 'A', 'B', 'R1', 'R2', 'R3', 'P']
        },
        'Ligero': {
            'usecols': 'B,G,O,Q,S',
            'names': ['Posicion', 'R0', 'R4', 'R5', 'S']
        }
    },
    
    # GRÁFICAS CON BARRAS DE ERROR - DOS LÍNEAS (PESADO Y LIGERO)
    'Rho vs Potencia Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Rho vs Potencia',
        'xlabel': 'Potencia (%)',
        'ylabel': 'Rho (Δk/k)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Fuel Temp vs Rho Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Fuel Temp vs Rho',
        'xlabel': 'Fuel Temp (Kº)',
        'ylabel': 'Rho (Δk/k)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Mod Temp vs Rho Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Mod Temp vs Rho',
        'xlabel': 'Mod Temp (Kº)',
        'ylabel': 'Rho (Δk/k)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Fuel Temp vs Potencia Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Fuel Temp vs Potencia',
        'xlabel': 'Fuel Temp (Kº)',
        'ylabel': 'Potencia (%)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Mod Temp vs Potencia Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Mod Temp vs Potencia',
        'xlabel': 'Mod Temp (Kº)',
        'ylabel': 'Potencia (%)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Reactividad vs Posición Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Reactividad vs Posición',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Reactividad (Δk/k)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Periodo vs Posición Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Periodo vs Posición',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Periodo (s)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Potencia vs Posición Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Potencia vs Posición',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Potencia (%)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Fuel Temp vs Posición Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Fuel Temp vs Posición',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Fuel Temp (Kº)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    },
    
    'Mod Temp vs Posición Barras de Error': {
        'tipo': 'con_error',
        'hoja_excel': 'Mod Temp vs Posición',
        'xlabel': 'Posición (cm)',
        'ylabel': 'Mod Temp (Kº)',
        'log_scale': False,
        'es_log_opcional': False,
        'datos_grafica': {
            'pesado': {
                'x': 'C64:D93',
                'y': 'G64:H93',
            },
            'ligero': {
                'x': 'A64:B93',
                'y': 'E64:F93',
            }
        },
        'barras_error': {
            'pesado': {
                'x': 'V133:V162',  # Barras de error para eje X Pesado
                'y': 'V99:V128'    # Barras de error para eje Y Pesado
            },
            'ligero': {
                'x': 'X133:X162',  # Barras de error para eje X Ligero  
                'y': 'X99:X128'    # Barras de error para eje Y Ligero
            }
        }
    }
}

def get_color(series_name):
    
    return COLOR_MAPPING.get(series_name, '#333333')

def cargar_datos_con_error(file_path, hoja_config):
    
    config = CONFIGURACION[hoja_config]
    
    try:
        import openpyxl
        
        hoja_excel = config.get('hoja_excel', hoja_config)
        print(f"  📊 Leyendo datos de la hoja: '{hoja_excel}'")
        
        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheet = wb[hoja_excel]
        
        datos_graf = config['datos_grafica']
        barras_error = config['barras_error']
        
        def extraer_datos_rango(rango):
            """Extrae datos de un rango específico usando openpyxl"""
            inicio, fin = rango.split(':')
            col_inicio = ''.join([c for c in inicio if c.isalpha()])
            fila_inicio = int(''.join([c for c in inicio if c.isdigit()]))
            col_fin = ''.join([c for c in fin if c.isalpha()])
            fila_fin = int(''.join([c for c in fin if c.isdigit()]))
            
            datos = []
            for row in range(fila_inicio, fila_fin + 1):
                fila_datos = []
                for col in [col_inicio, col_fin]:
                    celda = f"{col}{row}"
                    try:
                        valor = sheet[celda].value
                        fila_datos.append(valor)
                    except:
                        fila_datos.append(None)
                datos.append(fila_datos)
            return datos

        def extraer_datos_columna(rango):
            """Extrae datos de una sola columna"""
            inicio, fin = rango.split(':')
            col = ''.join([c for c in inicio if c.isalpha()])
            fila_inicio = int(''.join([c for c in inicio if c.isdigit()]))
            fila_fin = int(''.join([c for c in fin if c.isdigit()]))
            
            datos = []
            for row in range(fila_inicio, fila_fin + 1):
                celda = f"{col}{row}"
                try:
                    valor = sheet[celda].value
                    datos.append(valor)
                except:
                    datos.append(None)
            return datos

        def limpiar_datos_completo(x, y, error_x, error_y, hoja_config=None):
            """Limpia datos convirtiendo a float y eliminando valores inválidos para todos los arrays"""
            print(f"  Diagnóstico antes de limpiar:")
            print(f"    x: {len(x)} puntos")
            print(f"    y: {len(y)} puntos") 
            print(f"    error_x: {len(error_x)} puntos")
            print(f"    error_y: {len(error_y)} puntos")
            
            def convertir_a_float(arr):
                result = []
                for i, val in enumerate(arr):
                    try:
                        if val is None:
                            result.append(np.nan)
                        elif isinstance(val, (int, float)):
                            result.append(float(val))
                        elif isinstance(val, str):
                            cleaned_val = val.strip()
                            if cleaned_val == '':
                                result.append(np.nan)
                            else:
                                result.append(float(cleaned_val))
                        else:
                            result.append(float(val))
                    except (ValueError, TypeError) as e:
                        print(f"    Punto {i}: No se pudo convertir '{val}' (tipo {type(val)}) a float")
                        result.append(np.nan)
                return np.array(result)
            
            x_clean = convertir_a_float(x)
            y_clean = convertir_a_float(y) 
            error_x_clean = convertir_a_float(error_x)
            error_y_clean = convertir_a_float(error_y)
            
            mask = (~np.isnan(x_clean) & ~np.isnan(y_clean) & 
                    ~np.isnan(error_x_clean) & ~np.isnan(error_y_clean))
            mask = mask & (error_x_clean >= 0) & (error_y_clean >= 0)
            
            if hoja_config and 'Periodo vs Posición Barras de Error' in hoja_config:
                if len(mask) > 0:
                    mask[-1] = False
                    print(f"Descartado último punto para {hoja_config}")
            
            valid_count = np.sum(mask)
            print(f"  Después de limpiar: {valid_count} puntos válidos de {len(mask)}")
            
            if valid_count > 0:
                print(f"  Primeros puntos válidos:")
                print(f"    x: {x_clean[mask][:3]}")
                print(f"    y: {y_clean[mask][:3]}")
                print(f"    error_x: {error_x_clean[mask][:3]}")
                print(f"    error_y: {error_y_clean[mask][:3]}")
            else:
                print(f"No hay puntos válidos después de la limpieza")
            
            return (x_clean[mask], y_clean[mask], 
                    error_x_clean[mask], error_y_clean[mask])
        
        print(f"Cargando datos Pesado...")
        x_pesado_data = extraer_datos_rango(datos_graf['pesado']['x'])
        y_pesado_data = extraer_datos_rango(datos_graf['pesado']['y'])
        error_x_pesado_data = extraer_datos_columna(barras_error['pesado']['x'])
        error_y_pesado_data = extraer_datos_columna(barras_error['pesado']['y'])
        
        x_pesado = [row[0] for row in x_pesado_data if row[0] is not None]
        y_pesado = [row[0] for row in y_pesado_data if row[0] is not None]
        
        print(f"  Datos Pesado procesados: X={len(x_pesado)}, Y={len(y_pesado)}, Error_X={len(error_x_pesado_data)}, Error_Y={len(error_y_pesado_data)}")

        print(f"Cargando datos Ligero...")
        x_ligero_data = extraer_datos_rango(datos_graf['ligero']['x'])
        y_ligero_data = extraer_datos_rango(datos_graf['ligero']['y'])
        error_x_ligero_data = extraer_datos_columna(barras_error['ligero']['x'])
        error_y_ligero_data = extraer_datos_columna(barras_error['ligero']['y'])
        
        x_ligero = [row[0] for row in x_ligero_data if row[0] is not None]
        y_ligero = [row[0] for row in y_ligero_data if row[0] is not None]
        
        print(f"  Datos Ligero procesados: X={len(x_ligero)}, Y={len(y_ligero)}, Error_X={len(error_x_ligero_data)}, Error_Y={len(error_y_ligero_data)}")

        x_pesado, y_pesado, error_x_pesado, error_y_pesado = limpiar_datos_completo(
            x_pesado, y_pesado, error_x_pesado_data, error_y_pesado_data, hoja_config)
        
        x_ligero, y_ligero, error_x_ligero, error_y_ligero = limpiar_datos_completo(
            x_ligero, y_ligero, error_x_ligero_data, error_y_ligero_data, hoja_config)

        wb.close()
        
        datos_pesado = {
            'x': x_pesado, 
            'y': y_pesado, 
            'error_x': error_x_pesado,
            'error_y': error_y_pesado
        }
        datos_ligero = {
            'x': x_ligero, 
            'y': y_ligero, 
            'error_x': error_x_ligero,
            'error_y': error_y_ligero
        }
        
        print(f"Datos cargados: Pesado={len(x_pesado)} puntos, Ligero={len(x_ligero)} puntos")
        return datos_pesado, datos_ligero, config
        
    except Exception as e:
        print(f"Error cargando datos con error para {hoja_config}: {str(e)}")
        raise

def cargar_datos(file_path, hoja, grupo):
    """
    Carga datos desde archivo Excel según la configuración especificada
    """
    config = CONFIGURACION[hoja]
    
    # Si es gráfica con error, usar función específica
    if config['tipo'] == 'con_error':
        datos_pesado, datos_ligero, config = cargar_datos_con_error(file_path, hoja)
        return (datos_pesado, datos_ligero), config
    
    grupo_config = config[grupo]
    
    # Estrategia 1: Carga por rangos específicos
    if 'rangos' in grupo_config:
        datos = {}
        for nombre_serie, rango in grupo_config['rangos'].items():
            try:
                # Parsear rango (ej: 'B3:C303' -> columna B-C, filas 3-303)
                inicio, fin = rango.split(':')
                col_inicio = ''.join([c for c in inicio if c.isalpha()])
                fila_inicio = int(''.join([c for c in inicio if c.isdigit()]))
                col_fin = ''.join([c for c in fin if c.isalpha()])
                fila_fin = int(''.join([c for c in fin if c.isdigit()]))
                
                # Leer rango del Excel
                df = pd.read_excel(
                    file_path,
                    sheet_name=hoja,
                    header=None,
                    usecols=f"{col_inicio}:{col_fin}",
                    skiprows=fila_inicio-1,
                    nrows=fila_fin-fila_inicio+1,
                    engine='openpyxl'
                )
                
                if hoja == 'Periodo vs Rho':
                    df.columns = ['Periodo', 'Rho']
                elif hoja == 'Rho vs Potencia':
                    df.columns = ['Potencia', 'Rho']
                else:
                    df.columns = ['X', 'Y']
                
                datos[nombre_serie] = df.dropna()
                
            except Exception as e:
                print(f"Error procesando rango {rango} para {nombre_serie}: {str(e)}")
                continue
                
        return datos, config
        
    else:
        df = pd.read_excel(
            file_path,
            sheet_name=hoja,
            usecols=grupo_config['usecols'],
            skiprows=3,
            nrows=300,
            engine='openpyxl'
        )
        df.columns = grupo_config['names']
        return df, config
