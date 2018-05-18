def health(self, screen):
        if self.HP <= 80:
                pygame.draw.rect(screen, WHITE, [self.rect.x+29, self.rect.y-10, 6, 5], 0)
                if self.HP <= 60:
                    pygame.draw.rect(screen, WHITE, [self.rect.x+23, self.rect.y-10, 6, 5], 0)
                    if self.HP <= 40:
                        pygame.draw.rect(screen, WHITE, [self.rect.x+17, self.rect.y-10, 6, 5], 0)
                        if self.HP <= 20:
                            pygame.draw.rect(screen, WHITE, [self.rect.x+11, self.rect.y-10, 6, 5], 0)


          
        player.health(screen)               # This draws white (alternatively other background colour) over
                                          # original health bars to simulate the bars disappearing          
                #Enemy health bar
        for enemy in enemy_list:
            if enemy.HP <= 80:
                pygame.draw.rect(screen, WHITE, [enemy.rect.x+29, enemy.rect.y-10, 6, 5], 0)
                if enemy.HP <= 60:
                    pygame.draw.rect(screen, WHITE, [enemy.rect.x+23, enemy.rect.y-10, 6, 5], 0)
                    if enemy.HP <= 40:
                        pygame.draw.rect(screen, WHITE, [enemy.rect.x+17, enemy.rect.y-10, 6, 5], 0)
                        if enemy.HP <= 20:
                            pygame.draw.rect(screen, WHITE, [enemy.rect.x+11, enemy.rect.y-10, 6, 5], 0)
                            if enemy.HP <= 0:
                                pygame.draw.rect(screen, WHITE, [enemy.rect.x+5, enemy.rect.y-10, 10, 5], 0)
                                all_sprites_list.remove(enemy)
                                enemy_list.remove(enemy)
