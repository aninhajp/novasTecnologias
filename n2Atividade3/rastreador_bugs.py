import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados_bugs = {
    'Bug_ID': [f'BUG-{i}' for i in range(1, 16)],
    'Módulo': ['Backend', 'Frontend', 'DB', 'Backend', 'Frontend', 
               'DB', 'Backend', 'Frontend', 'Backend', 'DB', 
               'Frontend', 'Backend', 'DB', 'Frontend', 'Backend'],
    'Severidade': ['Alta', 'Baixa', 'Média', 'Alta', 'Média', 
                   'Baixa', 'Alta', 'Alta', 'Baixa', 'Média', 
                   'Baixa', 'Média', 'Alta', 'Média', 'Alta'],
    'Tempo_Resolucao_Horas': [24, 4, 12, np.nan, 8, 
                              6, -5, 16, 3, 14, 
                              2, 10, 36, 5, 18]
}

df_bugs = pd.DataFrame(dados_bugs)

df_bugs.loc[df_bugs['Tempo_Resolucao_Horas'] < 0, 'Tempo_Resolucao_Horas'] = np.nan

media_geral = df_bugs['Tempo_Resolucao_Horas'].mean()

df_bugs['Tempo_Resolucao_Horas'] = df_bugs['Tempo_Resolucao_Horas'].fillna(media_geral)

tempo_medio_modulo = df_bugs.groupby('Módulo')['Tempo_Resolucao_Horas'].mean().sort_values(ascending=False)
print("Tempo Médio de Resolução por Módulo:")
print(tempo_medio_modulo)

plt.figure(figsize=(8, 5))
tempo_medio_modulo.plot(kind='bar', color=['#ff4d4d', '#ffaa00', '#3399ff'])

plt.title('Tempo Médio de Resolução de Bugs por Módulo')
plt.xlabel('Módulo')
plt.ylabel('Tempo Médio (Horas)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()