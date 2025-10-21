import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator
from matplotlib.ticker import AutoMinorLocator, LogLocator, NullFormatter
from Pdata_config import cargar_datos, get_color, CONFIGURACION
import os
import pandas as pd

# CONFIGURACIÓN INICIAL

RUTA_GUARDADO = r'C:\Users\Usuario\Documets'
os.makedirs(RUTA_GUARDADO, exist_ok=True)

plt.style.use('default')
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'mathtext.fontset': 'cm',
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'axes.linewidth': 0.8,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'legend.framealpha': 1.0,
    'legend.edgecolor': 'black',
    'legend.fontsize': 10,
})


def aplicar_estilo_unificado(ax, config, es_grafica_error=False):

    if not es_grafica_error:
        ax.set_xlabel(config['xlabel'], fontsize=12, labelpad=10)
        ax.set_ylabel(config['ylabel'], fontsize=12, labelpad=10)
    
    ax.xaxis.set_minor_locator(AutoMinorLocator(5))
    ax.yaxis.set_minor_locator(AutoMinorLocator(5))
    
    ax.grid(True, which='major', linestyle='--', linewidth=0.7, alpha=0.5)
    ax.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.3)
    
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.tick_params(axis='both', which='minor', labelsize=8)

def interpolar_serie(x, y):

    if len(x) >= 4:
        
        sorted_idx = np.argsort(x)
        x_sorted = x[sorted_idx]
        y_sorted = y[sorted_idx]
        
        unique_x, unique_idx = np.unique(x_sorted, return_index=True)
        if len(unique_x) < len(x_sorted):
            x_sorted = unique_x
            y_sorted = y_sorted[unique_idx]
        
        x_new = np.linspace(x_sorted.min(), x_sorted.max(), 2000)
        return x_new, PchipInterpolator(x_sorted, y_sorted)(x_new)
    
    return x, y

def procesar_grafica_con_error(ax_pesado, ax_ligero, datos_pesado, datos_ligero, config, usar_escala):
    
    if len(datos_pesado['x']) > 0 and len(datos_pesado['y']) > 0:
        line_pesado = ax_pesado.plot(datos_pesado['x'], datos_pesado['y'],
                                    color=get_color('Pesado'),
                                    linestyle='-',
                                    linewidth=2.5,
                                    marker='o',
                                    markersize=6,
                                    markeredgecolor='black',
                                    markeredgewidth=0.5,
                                    alpha=0.8,
                                    label='Pesado')
        
        if len(datos_pesado['error_x']) > 0 and len(datos_pesado['error_y']) > 0:
            ax_pesado.errorbar(datos_pesado['x'], datos_pesado['y'], 
                            xerr=datos_pesado['error_x'],
                            yerr=datos_pesado['error_y'],
                            fmt='none',
                            ecolor=get_color('Pesado'),
                            elinewidth=1.5,
                            capsize=4,
                            capthick=1.5,
                            alpha=0.7,
                            label='_Error Pesado')

    if len(datos_ligero['x']) > 0 and len(datos_ligero['y']) > 0:
        line_ligero = ax_ligero.plot(datos_ligero['x'], datos_ligero['y'],
                                    color=get_color('Ligero'),
                                    linestyle='-',
                                    linewidth=2.5,
                                    marker='s',
                                    markersize=6,
                                    markeredgecolor='black',
                                    markeredgewidth=0.5,
                                    alpha=0.8,
                                    label='Ligero')
        
        if len(datos_ligero['error_x']) > 0 and len(datos_ligero['error_y']) > 0:
            ax_ligero.errorbar(datos_ligero['x'], datos_ligero['y'], 
                            xerr=datos_ligero['error_x'],
                            yerr=datos_ligero['error_y'],
                            fmt='none',
                            ecolor=get_color('Ligero'),
                            elinewidth=1.5,
                            capsize=4,
                            capthick=1.5,
                            alpha=0.7,
                            label='_Error Ligero')
    
    ax_pesado.set_xlabel(f"{config['xlabel']} (Pesado)", fontsize=11, labelpad=10, color=get_color('Pesado'))
    ax_pesado.set_ylabel(f"{config['ylabel']} (Pesado)", fontsize=11, labelpad=10, color=get_color('Pesado'))
    
    ax_pesado.tick_params(axis='x', colors=get_color('Pesado'))
    ax_pesado.tick_params(axis='y', colors=get_color('Pesado'))
    
    ax_ligero.set_xlabel(f"{config['xlabel']} (Ligero)", fontsize=11, labelpad=10, color=get_color('Ligero'))
    ax_ligero.set_ylabel(f"{config['ylabel']} (Ligero)", fontsize=11, labelpad=10, color=get_color('Ligero'))
    
    ax_ligero.tick_params(axis='x', colors=get_color('Ligero'))
    ax_ligero.tick_params(axis='y', colors=get_color('Ligero'))
    
    ax_pesado.spines['left'].set_position(('outward', 0))
    ax_pesado.spines['bottom'].set_position(('outward', 0))
    ax_pesado.spines['left'].set_color(get_color('Pesado'))
    ax_pesado.spines['bottom'].set_color(get_color('Pesado'))
    
    ax_ligero.spines['right'].set_position(('outward', 0))
    ax_ligero.spines['top'].set_position(('outward', 0))
    ax_ligero.spines['right'].set_color(get_color('Ligero'))
    ax_ligero.spines['top'].set_color(get_color('Ligero'))
    
    ax_ligero.spines['right'].set_visible(True)
    ax_ligero.spines['top'].set_visible(True)
    
    ax_pesado.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.3)
    ax_pesado.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.2)
    
    ax_ligero.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.3)
    ax_ligero.grid(True, which='minor', linestyle=':', linewidth=0.3, alpha=0.2)
    
    ax_pesado.legend(frameon=True, edgecolor='black', facecolor='white',
                    loc='upper left', fontsize=9)
    ax_ligero.legend(frameon=True, edgecolor='black', facecolor='white',
                    loc='upper right', fontsize=9)
    
    if len(datos_pesado['x']) > 0 and len(datos_pesado['y']) > 0:
        x_pesado_min = min(datos_pesado['x']) - max(datos_pesado['error_x']) if len(datos_pesado['error_x']) > 0 else min(datos_pesado['x'])
        x_pesado_max = max(datos_pesado['x']) + max(datos_pesado['error_x']) if len(datos_pesado['error_x']) > 0 else max(datos_pesado['x'])
        y_pesado_min = min(datos_pesado['y']) - max(datos_pesado['error_y']) if len(datos_pesado['error_y']) > 0 else min(datos_pesado['y'])
        y_pesado_max = max(datos_pesado['y']) + max(datos_pesado['error_y']) if len(datos_pesado['error_y']) > 0 else max(datos_pesado['y'])
        
        ax_pesado.set_xlim(x_pesado_min, x_pesado_max)
        ax_pesado.set_ylim(y_pesado_min, y_pesado_max)
    
    if len(datos_ligero['x']) > 0 and len(datos_ligero['y']) > 0:
        x_ligero_min = min(datos_ligero['x']) - max(datos_ligero['error_x']) if len(datos_ligero['error_x']) > 0 else min(datos_ligero['x'])
        x_ligero_max = max(datos_ligero['x']) + max(datos_ligero['error_x']) if len(datos_ligero['error_x']) > 0 else max(datos_ligero['x'])
        y_ligero_min = min(datos_ligero['y']) - max(datos_ligero['error_y']) if len(datos_ligero['error_y']) > 0 else min(datos_ligero['y'])
        y_ligero_max = max(datos_ligero['y']) + max(datos_ligero['error_y']) if len(datos_ligero['error_y']) > 0 else max(datos_ligero['y'])
        
        ax_ligero.set_xlim(x_ligero_min, x_ligero_max)
        ax_ligero.set_ylim(y_ligero_min, y_ligero_max)

def procesar_grafica_general_dataframe(ax, df, config, usar_escala):
    x_min, x_max = np.inf, -np.inf
    y_min, y_max = np.inf, -np.inf
    
    for i, col in enumerate(df.columns[1:]):
        mask = ~df[col].isna()
        x_vals = df['Posicion'][mask].values
        y_vals = df[col][mask].values
        
        if len(x_vals) > 0:
            if len(x_vals) > 1000:
                step = max(1, len(x_vals) // 200)
                x_vals = x_vals[::step]
                y_vals = y_vals[::step]
                
            sort_idx = np.argsort(x_vals)
            x_vals, y_vals = x_vals[sort_idx], y_vals[sort_idx]
            
            ax.plot(x_vals, y_vals,
                color=get_color(col),
                linestyle='-',
                linewidth=2.5,
                marker='o',
                markersize=6,
                markeredgecolor='black',
                markeredgewidth=0.5,
                alpha=0.8,
                label=col)
            
            x_min, x_max = min(x_min, df['Posicion'][mask].min()), max(x_max, df['Posicion'][mask].max())
            y_min, y_max = min(y_min, df[col][mask].min()), max(y_max, df[col][mask].max())
    
    if x_min != np.inf:
        x_range = x_max - x_min
        margin = 0.05 * x_range if x_range > 0 else 0.1
        ax.set_xlim(left=x_min - margin, right=x_max + margin)
    
    if y_min != np.inf:
        if usar_escala:
            ax.set_yscale('log')
            y_range_log = np.log10(y_max) - np.log10(y_min) if y_min > 0 and y_max > y_min else 1.0
            ax.set_ylim(bottom=max(y_min/10**y_range_log, 1e-10), top=y_max*10**(0.2*y_range_log))
        else:
            y_range = y_max - y_min
            margin = 0.05 * y_range if y_range > 0 else 0.1
            ax.set_ylim(bottom=y_min - margin, top=y_max + margin)
    
    aplicar_estilo_unificado(ax, config)
    
    if len(df.columns) > 1:
        ax.legend(
            frameon=True,
            edgecolor='black',
            facecolor='white',
            fontsize=9,
            loc='upper right',
            bbox_to_anchor=(1.15, 1),
            borderpad=0.6,
            handletextpad=0.5
        )

def procesar_grafica_general_diccionario(ax, datos, config, usar_escala):
    x_min, x_max = np.inf, -np.inf
    y_min, y_max = np.inf, -np.inf
    
    orden_series = ['A', 'B', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'S', 'P']
    series_mostrar = [s for s in orden_series if s in datos]
    
    for nombre_serie in series_mostrar:
        df = datos[nombre_serie].copy()
        
        if 'Temp' in df.columns and 'Rho' in df.columns:
            df_clean = df[['Temp', 'Rho']].dropna()
            x_vals = df_clean['Temp'].values
            y_vals = df_clean['Rho'].values
        elif 'Potencia' in df.columns and 'Rho' in df.columns:
            df_clean = df[['Potencia', 'Rho']].dropna()
            x_vals = df_clean['Potencia'].values
            y_vals = df_clean['Rho'].values
        else:
            df_clean = df.dropna()
            x_vals = df_clean.iloc[:, 0].values
            y_vals = df_clean.iloc[:, 1].values
        
        if len(x_vals) < 2:
            continue

        if len(x_vals) > 1:
            x_vals = x_vals[1:]
            y_vals = y_vals[1:]
        else:
            continue
        
        ax.plot(x_vals, y_vals,
            '-',
            color=get_color(nombre_serie),
            linewidth=2.5,
            marker='o',
            markersize=6,
            markeredgecolor='black',
            markeredgewidth=0.5,
            alpha=0.8,
            label=nombre_serie)
        
        x_min, x_max = min(x_min, x_vals.min()), max(x_max, x_vals.max())
        y_min, y_max = min(y_min, y_vals.min()), max(y_max, y_vals.max())
    
    ax.set_xlabel(config['xlabel'], fontsize=12, labelpad=10)
    ax.set_ylabel(config['ylabel'], fontsize=12, labelpad=10)
    
    x_margin = 0.05 * (x_max - x_min) if x_max != x_min else 0.1
    y_margin = 0.05 * (y_max - y_min) if y_max != y_min else 0.1
    
    ax.set_xlim(left=x_min - x_margin, right=x_max + x_margin)
    
    if usar_escala:
        ax.set_yscale('log')
        ax.set_ylim(bottom=max(y_min/1.1, 1e-10), top=y_max*1.1)
    else:
        ax.set_ylim(bottom=y_min - y_margin, top=y_max + y_margin)
    
    aplicar_estilo_unificado(ax, config)
    
    if series_mostrar:
        ax.legend(frameon=True, edgecolor='black', facecolor='white',
                loc='upper right', bbox_to_anchor=(1.15, 1), fontsize=9)

def procesar_grafica_especial_periodo(ax, resultado, config):

    x_min, x_max = np.inf, -np.inf
    y_min, y_max = np.inf, -np.inf
    
    for nombre_serie, df in resultado.items():
        
        x_col = 'Periodo' if 'Periodo' in df.columns else 'X'
        y_col = 'Rho' if 'Rho' in df.columns else 'Y'
        
        mask = (~df[x_col].isna()) & (~df[y_col].isna())
        x_vals = df[x_col][mask].values
        y_vals = df[y_col][mask].values
        
        if len(x_vals) > 0:
            sort_idx = np.argsort(x_vals)
            x_vals = x_vals[sort_idx]
            y_vals = y_vals[sort_idx]
            
            ax.plot(y_vals, x_vals,
                color=get_color(nombre_serie),
                linestyle='-',
                linewidth=2.5,
                marker='o',
                markersize=6,
                markeredgecolor='black',
                markeredgewidth=0.5,
                alpha=0.8,
                label=nombre_serie)
            
            x_min, x_max = min(x_min, y_vals.min()), max(x_max, y_vals.max())
            y_min, y_max = min(y_min, x_vals.min()), max(y_max, x_vals.max())
    
    
    ax.set_xlabel(config['xlabel'], fontsize=12, labelpad=10)
    ax.set_ylabel(config['ylabel'], fontsize=12, labelpad=10)
    
    if x_min != np.inf and x_max != -np.inf:
        x_margin = 0.05 * (x_max - x_min) if x_max != x_min else 0.1
        ax.set_xlim(left=x_min - x_margin, right=x_max + x_margin)
    
    if y_min != np.inf and y_max != -np.inf:
        y_margin = 0.05 * (y_max - y_min) if y_max != y_min else 0.1
        ax.set_ylim(bottom=y_min - y_margin, top=y_max + y_margin)
    
    aplicar_estilo_unificado(ax, config)
    
    if ax.get_legend_handles_labels()[0]:
        ax.legend(
            frameon=True,
            edgecolor='black',
            facecolor='white',
            fontsize=9,
            loc='upper right',
            bbox_to_anchor=(1.15, 1),
            borderpad=0.6,
            handletextpad=0.5
        )

def procesar_grafica_especial_potencia(ax, resultado, config):

    for col in resultado.columns[1:]:
        puntos = resultado[['Posicion', col]].dropna()
        
        ax.plot(puntos[col], puntos['Posicion'], 
            'r-', linewidth=2.5, label=col)
        ax.scatter(puntos[col], puntos['Posicion'], 
                c='red', s=50, edgecolor='black')
    
    ax.set_xlabel(config['xlabel'])
    ax.set_ylabel(config['ylabel'])
    ax.grid(True)
    ax.legend()

    aplicar_estilo_unificado(ax, config)

def generar_grafica(file_path, hoja, grupo, escala_log=True):
    try:
        config = CONFIGURACION[hoja]
        
        usar_escala = config.get('log_scale', escala_log) if 'log_scale' in config else escala_log
        
        sufijo = 'log' if usar_escala else 'lin'

        resultado, config = cargar_datos(file_path, hoja, grupo)
        
        fig, ax = plt.subplots(figsize=(12, 7))
        
        ax.set_xlabel(config['xlabel'], fontsize=12)
        ax.set_ylabel(config['ylabel'], fontsize=12)
        
        if config['tipo'] == 'con_error':
            datos_pesado, datos_ligero = resultado
            
            fig, ax_pesado = plt.subplots(figsize=(14, 8))
            
            ax_ligero = ax_pesado.twinx().twiny()
            
            nombre_base = hoja.replace(' Barras de Error', '')
            
            procesar_grafica_con_error(ax_pesado, ax_ligero, datos_pesado, datos_ligero, config, usar_escala)
            
            nombre_archivo = f"{hoja.replace(' ', '_')}_{sufijo}.png"
            plt.savefig(os.path.join(RUTA_GUARDADO, nombre_archivo), dpi=600, bbox_inches='tight')
            plt.close()
            
            print(f"Gráfica guardada: {nombre_archivo}")
            return True
        
        else:
            if config['tipo'] == 'especial_periodo':
                procesar_grafica_especial_periodo(ax, resultado, config)
            elif config['tipo'] == 'especial_potencia':
                procesar_grafica_especial_potencia(ax, resultado, config)
            else:
                if isinstance(resultado, pd.DataFrame):
                    procesar_grafica_general_dataframe(ax, resultado, config, usar_escala)
                else:
                    procesar_grafica_general_diccionario(ax, resultado, config, usar_escala)
            
            ax.grid(True, which='major', linestyle='--', linewidth=0.6, alpha=0.5)
            ax.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.3)
            
            if ax.get_legend_handles_labels()[0]:
                ax.legend(
                    frameon=True,
                    edgecolor='black',
                    facecolor='white',
                    loc='upper right',
                    bbox_to_anchor=(1.15, 1),
                    borderpad=0.6,
                    handletextpad=0.5
                )
            
            plt.tight_layout(rect=[0, 0, 0.88, 1])
            
            nombre_archivo = f"{hoja.replace(' ', '_')}_{grupo}_{sufijo}.png"
            plt.savefig(os.path.join(RUTA_GUARDADO, nombre_archivo), dpi=600, bbox_inches='tight')
            plt.close()
            
            print(f"Gráfica guardada: {nombre_archivo}")
            return True
        
    except Exception as e:
        print(f"\nError al procesar {hoja}: {str(e)}")
        raise


if __name__ == "__main__":
    file_path = r'C:\Users\Usuario\Documets\Documento.xlsx'
    
    print("Iniciando generación de gráficas...")
    
    for hoja, config in CONFIGURACION.items():
        if config['tipo'] == 'con_error':
            print(f"\nProcesando gráfica con barras de error: {hoja}...")
            generar_grafica(file_path, hoja, 'Pesado', escala_log=True)
        else:
            for grupo in ['Pesado', 'Ligero']:
                if grupo in config:
                    if config.get('es_log_opcional', True):
                        for escala in [False, True]:
                            print(f"\nProcesando: {hoja} - {grupo} - {'Log' if escala else 'Lin'}...")
                            generar_grafica(file_path, hoja, grupo, escala_log=escala)
                    else:
                        if 'log_scale' in config:
                            escala = config['log_scale']
                            print(f"\nProcesando: {hoja} - {grupo} - {'Log' if escala else 'Lin'}...")
                            generar_grafica(file_path, hoja, grupo, escala_log=escala)
                        else:
                            for escala in [False, True]:
                                print(f"\nProcesando: {hoja} - {grupo} - {'Log' if escala else 'Lin'}...")
                                generar_grafica(file_path, hoja, grupo, escala_log=escala)
    
    print("\n¡Proceso completado con éxito!")
